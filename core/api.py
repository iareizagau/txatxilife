from django.shortcuts import render
from ninja import NinjaAPI, Form
from ninja.security import django_auth
from ninja.security import HttpBearer, HttpBasicAuth
from apps.maps.api import router as maps_router
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token


class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        if username == "admin" and password == "secret":
            return username


api = NinjaExtraAPI(auth=AuthBearer(),
                    title='TxatxiLife',
                    description='Asteburutako planen mapa',
                    openapi_extra={'info': {"termsOfService": "https://example.com/terms/", }},
                    version='1.0.1',
                    )

api.register_controllers(NinjaJWTDefaultController)
api.add_router("/map/", maps_router, tags=["maps"])  # You can add a router as an object


@api.get("/hello", auth=None)
def health(request):
    return "hello"


@api.get("/auth", auth=django_auth)
def health(request):
    return f"Authenticated user {request.auth}"


@api.get("/token", auth=BasicAuth())
def basic(request):
    return {"token": "supersecret"}


@api.get("/bearer", auth=AuthBearer())
def bearer(request):
    return {"token": request.auth}


def ip_whitelist(request):
    if request.META["REMOTE_ADDR"] == "8.8.8.8":
        return "8.8.8.8"


@api.get("/ipwhitelist", auth=ip_whitelist)
def ipwhitelist(request):
    return f"Authenticated client, IP = {request.auth}"

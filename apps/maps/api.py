from ninja import Router
from ninja.security import HttpBearer, HttpBasicAuth
from ninja_extra import api_controller, route
from ninja_jwt.authentication import JWTAuth


class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
        if username == "admin" and password == "secret":
            return username


router = Router(auth=BasicAuth())


@router.get('/hello')
def maphello(request):
    return "hello maps"


@router.get('/some-endpoint', auth=JWTAuth())
def some_endpoint(request):
    return "holaaaaaaaaaa"

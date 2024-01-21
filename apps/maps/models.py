import os.path

from django.db import models
import uuid


def camper_night_point_upload_to(instance, filename):
    print(f"****{instance}, {filename}")
    return os.path.join('camper_night_point/', filename)


def interest_point_upload_to(instance, filename):
    print(f"****{instance}, {filename}")
    return os.path.join('interest_point/', filename)


class Category(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class InterestPoint(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class CamperNightPoint(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    free = models.BooleanField(default=False)
    wc = models.BooleanField(default=False)
    drinking_water = models.BooleanField(default=False)
    tables = models.BooleanField(default=False)
    gray_sink = models.BooleanField(default=False)
    black_sink = models.BooleanField(default=False)
    electricity = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ImageInterestPoint(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    interest_point_id = models.ForeignKey(InterestPoint, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=interest_point_id)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ImageCamperNightPoint(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    camper_night_point_id = models.ForeignKey(CamperNightPoint, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=camper_night_point_id)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

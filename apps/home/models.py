# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
import os


def upload_to(instance, filename):
    print(f"****{instance}, {filename}")
    path = os.path.join('background_images/', filename)
    return path


class ImageInterestPoint(models.Model):
    title = models.CharField(max_length=210)
    image = models.ImageField(upload_to=upload_to)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

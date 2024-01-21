from django.contrib import admin
from .models import Category, InterestPoint, ImageInterestPoint, CamperNightPoint, ImageCamperNightPoint


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Category, CategoryAdmin)


class InterestPointAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")


admin.site.register(InterestPoint, InterestPointAdmin)


class ImageInterestPointAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")


admin.site.register(ImageInterestPoint, ImageInterestPointAdmin)


class CamperNightPointAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")


admin.site.register(CamperNightPoint, CamperNightPointAdmin)

class ImageCamperNightPointAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")


admin.site.register(ImageCamperNightPoint, ImageCamperNightPointAdmin)


from django.contrib import admin
from .models import Category, InterestPoint, ImageInterestPoint, CamperNightPoint, ImageCamperNightPoint


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Category, CategoryAdmin)


class ImageInterestPointInline(admin.StackedInline):
    model = ImageInterestPoint


class InterestPointAdmin(admin.ModelAdmin):
    inlines = [ImageInterestPointInline]


admin.site.register(InterestPoint, InterestPointAdmin)


class CamperNightPointInline(admin.StackedInline):
    model = ImageCamperNightPoint


class CamperNightPointAdmin(admin.ModelAdmin):
    inlines = [CamperNightPointInline]


admin.site.register(CamperNightPoint, CamperNightPointAdmin)

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models


class ProductImageInline(admin.StackedInline):
    model = models.ProductImage
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    inlines = [ProductImageInline]


@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image', 'is_main', 'is_active', 'created', 'updated']


admin.site.register(models.Tag)
admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Feature)
admin.site.register(models.Configuration)
admin.site.register(models.PackageContent)
admin.site.register(models.Color)

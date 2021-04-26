from django.contrib import admin
from .models import Brand, Product
# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['name', 'created']
    list_filter = ['created']
    ordering = ['-created']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    list_display = ['name', 'price', 'brand', 'state', 'manufacturing']
    list_filter = ['brand', 'state']
    ordering = ['-created']
    search_fields = ['name']
    list_editable = ['price']

#admin.site.register(Brand, BrandAdmin)
#admin.site.register(Product, ProductAdmin)
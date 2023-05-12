from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from django.utils.safestring import mark_safe

from .models import *
# Register your models here.

admin.site.register(Brand)

class ProductsAdmin(TranslationAdmin):
    list_display = ['title', 'brand', 'quant', 'price',]            # 'get_image'
    list_filter = ("brand", 'size', 'gender')
    search_fields = ("title", "brand")
    readonly_fields = ("get_image",)


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="40" height="40"')
    
    get_image.short_description = "Изображение"

    fieldsets = (
        (None, {
            "fields": ( ('title',),
                        ('description',),
                        ('price',), 
                        ('size',),
                        ('quant',),
                        ('gender',),
        ("image", "get_image"),)
        }),

        ("Brand", {
            "classes": ("collapse",),
            "fields": (("brand",))
        }),
    )

admin.site.register(Products, ProductsAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'brand', 'quant', 'price']
    list_filter = ("brand", )
    search_fields = ('user', "brand") 

admin.site.register(Cart, CartAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',  'brand', 'quant', 'price']
    list_filter = ("brand", )
    search_fields = ('user', "brand")

admin.site.register(Order, OrderAdmin)

class FavAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']
admin.site.register(Favorite, FavAdmin )
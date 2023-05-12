from modeltranslation.translator import register, TranslationOptions
from .models import *



@register(Products)
class ProductsTranslationOptions(TranslationOptions):
    fields = ('description',)





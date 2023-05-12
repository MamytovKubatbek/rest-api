from django.shortcuts import render
# from rest_framework.generics import CreateAPIView, UpdateAPIView
# from rest_framework.views import APIView

from rest_framework import generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from .serializer import *

# Create your views here.

class ProductsPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000



class ProductsAPIList(generics.ListAPIView):
    
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('title', 'description', 'size', 'gender',)
    pagination_class = ProductsPagination



class BrandAPIList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('name',)



class OrderAPIList(generics.ListAPIView, mixins.CreateModelMixin , GenericAPIView   ):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class FavProductsAPIList(generics.ListAPIView, mixins.CreateModelMixin , GenericAPIView   ):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FavAPIList(generics.ListAPIView,mixins.RetrieveModelMixin, mixins.DestroyModelMixin , GenericAPIView   ):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CartProductsAPIList(generics.ListAPIView, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericAPIView    ):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class CartAPIList(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    
    GenericAPIView
):

    queryset = Cart.objects.all()
    serializer_class = CartSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)












# install

# pip install django-filter

# pip install rest-framework-pagination
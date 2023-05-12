from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductsAPIList.as_view(), name="home"),
    path('brand/', views.BrandAPIList.as_view(), name="Brand"),
    path('order/', views.OrderAPIList.as_view(), name="order"),

    path('fav/', views.FavProductsAPIList.as_view(), name="fav"),
    path('fav/<str:pk>/', views.FavAPIList.as_view(), name="fav"),

    path('cart/', views.CartProductsAPIList.as_view(), name="cart"),
    path('cart/<str:pk>/', views.CartAPIList.as_view(), name="cart"),
]




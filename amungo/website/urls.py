from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('product/<slug:product_slug>', views.product_page, name='product_page'),
]

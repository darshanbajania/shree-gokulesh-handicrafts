
from django.urls import path

from . import views

app_name = 'wagha'

urlpatterns = [
    path('', views.Home, name='home'),
    path('product_details', views.Product_details, name='product_details'),
    path('all_products', views.All_products, name='all_products'),
]
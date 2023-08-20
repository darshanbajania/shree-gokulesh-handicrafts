from django.shortcuts import render
from .models import Product
# Create your views here.
from django.http import HttpResponse


def home(request):
    product_data = Product.objects.all()
    print("🚀 ~ file: views.py:9 ~ productData:", product_data)
    context ={
        'product_data': product_data
    }
    return render(request, 'wagha/base.html', context=context)
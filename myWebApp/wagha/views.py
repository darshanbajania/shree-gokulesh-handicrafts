from django.shortcuts import render
from .models import Product, Advertisement, Color, Size, Material
# Create your views here.
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from urllib.parse import urlencode
import json

class cart_product:
    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

 
class CartProductEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, cart_product):
            return {'product_id': obj.product_id, 'quantity': obj.quantity}
        return super().default(obj)



def Home(request):
    product_data = Product.objects.all()
    homeAdvertisementImage = Advertisement.objects.filter(label='HomePage').first()
    if(request.session.has_key('cart_data') != True):
        request.session['cart_data'] = {} 

    if request.method == "POST":
            # cart_contents.clear()
            # print(cart_contents)
            # print(request.session['cart_contents'])
        product_id = request.POST.get('product')
        view_all_type = request.POST.get('view-all-button')
        card_action_type = request.POST.get('card_action_type')

                    
        if view_all_type != None:
            print(product_id)
            base_url = reverse('wagha:all_products')
            # creating a string of dictionary
            query_string = urlencode({'product': product_id})
            # passing the base_url and query from this page to url
            url = '{}?{}'.format(base_url, query_string)

            # print(proposal_number)
            return redirect(url)

        if card_action_type == 'add-to-cart' and product_id != None :
            if(request.session.has_key('cart_data')):

                cartData = request.session['cart_data']
                print("🚀 ~ file: views.py:43 ~ cartData:", cartData)
                cartContents = cartData
                product = cart_product(product_id, 1)
                serialized_product = json.dumps(product, cls=CartProductEncoder)
                cartContents[product_id]=serialized_product
                request.session['cart_data'] = cartContents
                print("🚀 ~ file: views.py:37 ~ cartProduct:", cartContents)

        if card_action_type == 'view-product' and product_id != None:
            # getting the url for displaying full proposal
            print(product_id)
            base_url = reverse('wagha:product_details')
            # creating a string of dictionary
            query_string = urlencode({'product': product_id})
            # passing the base_url and query from this page to url
            url = '{}?{}'.format(base_url, query_string)

            # print(proposal_number)
            return redirect(url)
    context ={
        'product_data': product_data,
        'banner_url':homeAdvertisementImage.image.url
    }
    return render(request, 'wagha/base.html', context=context)

def Product_details(request):
    current_product_id = request.GET.get('product')
    selected_product = Product.objects.filter(id=current_product_id).first()
    context ={
        'selected_product': selected_product,
    }

    return render(request, 'wagha/product_details.html', context=context)
def All_products(request):
        # print(current_product_id)
    all_products = Product.objects.all()

    if request.method == "POST":
            # cart_contents.clear()
            # print(cart_contents)
            # print(request.session['cart_contents'])
        product_id = request.POST.get('product')
        if product_id != None:
            # getting the url for displaying full proposal
            print(product_id)
            base_url = reverse('wagha:product_details')
            # creating a string of dictionary
            query_string = urlencode({'product': product_id})
            # passing the base_url and query from this page to url
            url = '{}?{}'.format(base_url, query_string)

            # print(proposal_number)
            return redirect(url)
    all_colors = Color.objects.all()
    all_sizes = Size.objects.all()
    all_materials = Material.objects.all()
    context ={
        'all_products': all_products,
        'all_colors': all_colors,
        'all_sizes': all_sizes,
        'all_materials': all_materials,
    }

    return render(request, 'wagha/all_products.html', context=context)
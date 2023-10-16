from django.shortcuts import render
from .models import Product, Advertisement, Color, Size, Material
# Create your views here.
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from urllib.parse import urlencode
import json
from django.db.models import F, Value, CharField


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
    cart_data = request.session.get('cart_data', {})
    for product in product_data:
        product.in_cart = str(product.id) in cart_data
    context ={
        'product_data': product_data,
        'banner_url':homeAdvertisementImage.image.url,
        'cart_items_count':len(request.session['cart_data']),
        'cart_data': request.session['cart_data']
    }
    return render(request, 'wagha/base.html', context=context)

def Product_details(request):
    current_product_id = request.GET.get('product')
    selected_product = Product.objects.filter(id=current_product_id).first()
    cart_data = request.session.get('cart_data', {})

        # Parse the JSON data within cart_item and retrieve the 'quantity' value
 
    if request.method == "POST":
        product_id = current_product_id

        if request.POST.get('add') != None:
            item_id = request.POST.get('product_id')
            cartContents = cart_data
            existingItem = cart_data.get(item_id)
            quantity = 0
            print('entered add')
            if existingItem:
                print('entered existing item')

                cart_item_dict = json.loads(existingItem)
                quantity = cart_item_dict.get('quantity', 0)
                product = cart_product(item_id, quantity+ 1)
                serialized_product = json.dumps(product, cls=CartProductEncoder)
                cartContents[item_id]=serialized_product
                print()
                request.session['cart_data'] = cartContents
            else:
                print('entered else of existing item')

                product = cart_product(product_id,  1)
                serialized_product = json.dumps(product, cls=CartProductEncoder)
                cartContents[product_id]=serialized_product
                print('entered else of existing item',cartContents )

                request.session['cart_data'] = cartContents
        if request.POST.get('minus') != None:
            item_id = request.POST.get('product_id')
            # print(type(item_id))
            # print(cart_contents.get(int(item_id)))
            cartContents = cart_data
            existingItem = cart_data.get(item_id)
            quantity = 0
            print('entered minus')
            if existingItem:
                cart_item_dict = json.loads(existingItem)
                quantity = cart_item_dict.get('quantity', 0)
                print('entered existing item')
                if(quantity >1):
                    product = cart_product(item_id, quantity- 1)
                    serialized_product = json.dumps(product, cls=CartProductEncoder)
                    cartContents[item_id]=serialized_product
                else:
                    del cartContents[item_id]
                    
                request.session['cart_data'] = cartContents
            # cart_data[item_id] = int(cart_data.get(item_id)) - 1
            # if cart_data[item_id] == 0:
            #     cart_data.pop(item_id)
            #     request.session['cart_data'] = cart_data
    quantity = 0
    cart_item = cart_data.get(current_product_id)

    if cart_item:
        cart_item_dict = json.loads(cart_item)
        quantity = cart_item_dict.get('quantity', 0)
    context ={
        'selected_product': selected_product,
        'quantity': quantity
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
        card_action_type = request.POST.get('card_action_type')
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
    all_colors = Color.objects.all()
    all_sizes = Size.objects.all()
    all_materials = Material.objects.all()
    cart_data = request.session.get('cart_data', {})
    for product in all_products:
        product.in_cart = str(product.id) in cart_data
    context ={
        'all_products': all_products,
        'all_colors': all_colors,
        'all_sizes': all_sizes,
        'all_materials': all_materials,
        'cart_items_count':len(request.session['cart_data']),
        'cart_data': request.session['cart_data']
    }

    return render(request, 'wagha/all_products.html', context=context)
def Cart_page(request):
        # print(current_product_id)
    cart_data = request.session.get('cart_data', {})

    cart_contents_description = []
    bill_description = []
    total_amount = 0
    if request.method == "POST":
        if request.POST.get('add') != None:
            item_id = request.POST.get('product_id')
            cartContents = cart_data
            existingItem = cart_data.get(item_id)
            quantity = 0
            if existingItem:
                cart_item_dict = json.loads(existingItem)
                quantity = cart_item_dict.get('quantity', 0)
                product = cart_product(item_id, quantity+ 1)
                serialized_product = json.dumps(product, cls=CartProductEncoder)
                cartContents[item_id]=serialized_product
                request.session['cart_data'] = cartContents
            else:
                
                product = cart_product(product_id,  1)
                serialized_product = json.dumps(product, cls=CartProductEncoder)
                cartContents[product_id]=serialized_product
                request.session['cart_data'] = cartContents
        if request.POST.get('minus') != None:
            item_id = request.POST.get('product_id')
            # print(type(item_id))
            # print(cart_contents.get(int(item_id)))
            cartContents = cart_data
            existingItem = cart_data.get(item_id)
            quantity = 0
            if existingItem:
                cart_item_dict = json.loads(existingItem)
                quantity = cart_item_dict.get('quantity', 0)
                if(quantity >1):
                    product = cart_product(item_id, quantity- 1)
                    serialized_product = json.dumps(product, cls=CartProductEncoder)
                    cartContents[item_id]=serialized_product
                else:
                    del cartContents[item_id]
                    
                request.session['cart_data'] = cartContents
            # cart_data[item_id] = int(cart_data.get(item_id)) - 1
            # if cart_data[item_id] == 0:
            #     cart_data.pop(item_id)
            #     request.session['cart_data'] = cart_data

            if request.POST.get('remove') != None:
                item_id = request.POST.get('product_id')
                # print(type(item_id))
                # print(cart_contents.get(int(item_id)))
                cart_data.pop(item_id)
                request.session['cart_contents'] = cart_data

    # print("🚀 ~ file: views.py:144 ~ product̥_quantities:", cart_data)

    all_products = Product.objects.filter(id__in=cart_data)
    product_data = []
    delivery_charge =75
    total_amount=0
    for product in all_products:
        product_id_str = str(product.id)
        cart_item = cart_data.get(product_id_str)

        # Parse the JSON data within cart_item and retrieve the 'quantity' value
        quantity = 0
        if cart_item:
            cart_item_dict = json.loads(cart_item)
            quantity = cart_item_dict.get('quantity', 0)
        total_amount += product.price * quantity
        product_data.append({
            'product': product,
            'quantity': quantity
        })
        
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

    context ={
        'all_products': all_products,
        'product_data': product_data,  # Add the combined data to the context
        'total_amount': total_amount+delivery_charge,
        'delivery_charge':delivery_charge

    }

    return render(request, 'wagha/cart.html', context=context)
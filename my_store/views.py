import json

from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from my_store.forms import ProductForm, CategoryForm
from my_store.models import *
from .serializers import ProductSerializer
from .utils import add_to_cart, remove_from_cart, update_cart, get_cart_items
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.contrib.auth import authenticate, login


# @csrf_exempt
# def register(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)  # Get JSON data from Postman
#             username = data.get('username')
#             email = data.get('email')
#             password = data.get('password')
#
#             # Check for required fields
#             if not username or not password:
#                 return JsonResponse({'error': 'Username and password are required'}, status=400)
#
#             # Check if the username already exists
#             if User.objects.filter(username=username).exists():
#                 return JsonResponse({'error': 'Username already exists'}, status=400)
#
#             # Validate email
#             if email and User.objects.filter(email=email).exists():
#                 return JsonResponse({'error': 'Email already in use'}, status=400)
#
#             # Create the user
#             User.objects.create_user(username=username, email=email, password=password)
#             return JsonResponse({'message': 'User registered successfully!'}, status=201)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON data'}, status=400)
#
#     return JsonResponse({'error': 'Invalid request method'}, status=405)
#
# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)  # Parse the JSON data
#             username = data.get('username')
#             password = data.get('password')
#
#             if not username or not password:
#                 return JsonResponse({'error': 'Username and password are required'}, status=400)
#
#             # Authenticate user
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 # Login successful
#                 request.session['user_id'] = user.id  # Save user ID in session
#                 return JsonResponse({'message': 'Login successful'}, status=200)
#             else:
#                 # Invalid credentials
#                 return JsonResponse({'error': 'Invalid username or password'}, status=401)
#
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON data'}, status=400)
#
#     return JsonResponse({'error': 'Invalid request method'}, status=405)
#
# def loguout(request):
#     logout(request)
#     return JsonResponse({'message': 'Logout successful'}, status=200)


@api_view(['GET'])
def product_list(request):
    query = request.GET.get('q', '')
    product = Product.objects.filter(name__icontains=query) if query else Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)




#####CMS Section
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the product to the database
            return redirect('product_list')  # Redirect to product list after saving
        else:
            print(form.errors)
    else:
        form = ProductForm()
    return render(request, 'my_store/add_product.html', {'form': form})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = CategoryForm()
        return render(request, 'my_store/categoriy_add.html', {"form": form})

@csrf_exempt
########### Cart section
def add_to_cart(request):
    if request.method== 'POST':
        product_id = request.POST.get('product_id')
        name = request.POST.get('name')
        price = (request.POST.get('price'))

        add_to_cart(request, product_id, name, price)
        return JsonResponse({'status': 'success'})
@csrf_exempt
def view_cart(request):
    if request.method== 'GET':
        cart_items = get_cart_items(request)
        total = sum( item['price'] * item['quantity'] for item in cart_items)
        return JsonResponse({"cart_items": cart_items, "total": total}, status=200)

def remove_cart(request, product_id):
    if request.method == 'DELETE':
        remove_from_cart(request, product_id)
        return JsonResponse({"message": "Item removed from cart"}, status=200)

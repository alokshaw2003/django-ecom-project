from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Product
from .cart import Cart

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    # Get quantity from the POST data, default to 1 if not found
    quantity = int(request.POST.get('quantity', 1))
    # Check if the 'update' flag is present in the POST data
    update_quantity = request.POST.get('update') == 'True'
    
    cart.add(product=product,
             quantity=quantity,
             update_quantity=update_quantity)
    
    messages.success(request, f'Cart updated for "{product.name}".')
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'"{product.name}" was removed from your cart.')
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'products/cart_detail.html', {'cart': cart})

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)
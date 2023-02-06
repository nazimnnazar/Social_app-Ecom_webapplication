from django.shortcuts import render,redirect
from core.models import*
from . models import *
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
# Create your views here.

def cart(request,tot=0,count=0,cart_item=None):
    try:
        cart = CartList.objects.get(cart_id = c_id(request))
        cart_item = CartItems.objects.filter(cart = cart)
        for i in cart_item:
            tot += (i.product.price * i.quantity)
            count += i.quantity
    except objectDoesNotExit:
        pass
    context ={
        'cartitem':cart_item,
        'total':tot,
        'count':count,
    }
    return render(request,'core/cart.html',context)

def c_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id

def addcart(request,product_id):
    product = Products.objects.get(id=product_id)
    try:
        cart = CartList.objects.get(cart_id=c_id(request))
    except CartList.DoesNotExist:
        cart = CartList.objects.create(cart_id=c_id(request))
        cart.save()
    try:
        cart_item = CartItems.objects.get(
                                        product=product,
                                        cart=cart
                                        )
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItems.DoesNotExist:
        cart_item = CartItems.objects.create(
                                            product=product,
                                            quantity=1,
                                            cart=cart
                                            )
        cart_item.save()
    return redirect('cart')


def direcmemt(request,product_id):
    cart = CartList.objects.get(cart_id=c_id(request))
    product = get_object_or_404(Products,id=product_id)
    cart_items = CartItems.objects.get(product=product,cart=cart)
    if cart_items.quantity >1:
        cart_items.quantity -=1
        cart_items.save()
    else:
        cart_items.delete()
    return redirect('cart')

def delete(request,product_id):
    cart = CartList.objects.get(cart_id=c_id(request))
    product = get_object_or_404(Products,id=product_id)
    cart_items = CartItems.objects.get(product=product,cart=cart)
    cart_items.delete()
    return redirect('cart')
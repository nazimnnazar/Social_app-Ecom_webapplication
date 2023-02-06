from django.shortcuts import render
from . models import*
# Create your views here.

def frontpage(request):
    return render(request,'home.html')

def product(request):
    product = Products.objects.all()
    context = {
        'product':product
    }
    return render(request,'core/product.html',context)

def productdetails(request,pk):
    productdetails = Products.objects.get(id=pk)
    context = {
        'productdetails':productdetails
    }
    return render(request,'core/productdetails.html',context)
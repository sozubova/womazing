from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from shop.models import Product, Category


# Create your views here.
def homepage(request):
    products = Product.objects.all()[:3]
    category = Category.objects.all()
    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'homepage.html', context)


def about_brand(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'about-brand.html', context)


def contacts(request):
    products = Product.objects.all()[:3]
    category = Category.objects.all()
    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'contacts.html', context)

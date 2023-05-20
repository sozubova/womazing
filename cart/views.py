from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ByersDetailForm
from .models import ByersData
from shop.models import Product, Category


# Create your views here.
def cart(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'cart/cart.html', context)


def checkout(request):
    products = Product.objects.all()
    category = Category.objects.all()
    if request.method == "POST":
        form = ByersDetailForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            byers_data = ByersData(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                country=form.cleaned_data['country'],
                city=form.cleaned_data['city'],
                street=form.cleaned_data['street'],
                house=form.cleaned_data['house'],
                flat=form.cleaned_data['flat'],
                message=form.cleaned_data['message'],
            )
            byers_data.save()
            return HttpResponseRedirect('/cart/success')
    else:
        form = ByersDetailForm()
    return render(request, 'cart/checkout.html', context={'form': form, 'products': products,
                                                          'category': category, })


def success(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {
        'products': products,
        'category': category,
    }
    return render(request, 'cart/order-success.html', context)

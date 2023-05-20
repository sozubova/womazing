from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Product, Category, Color
from .forms import ProductForm
from django.db.models import Max


# Create your views here.
def shop(request):
    products = Product.objects.all()[:9]
    category = Category.objects.all()
    shown_count = len(products)
    context = {
        'products': products,
        'category': category,
        'total': products.count(),
        'shown_count': shown_count,
        'max_id': products.aggregate(Max('id')),
    }
    return render(request, 'shop/all_products.html', context)


def shop_category(request, category_slug: str):
    categories = get_object_or_404(Category, slug=category_slug)
    category = Category.objects.all()
    products = Product.objects.filter(category=categories)
    shown_count = len(products)
    context = {
        'categories': categories,
        'category': category,
        'products': products,
        'shown_count': shown_count,
        'total': products.count(),
        'max_id': products.aggregate(Max('id')),
    }
    return render(request, 'shop/categories.html', context)


def one_item(request, category_slug: str, prod_slug: str):
    # products = get_object_or_404(Product, slug=prod_slug)
    # category = get_object_or_404(Category, categories__slug=category_slug, slug=prod_slug)
    category = Category.objects.all()
    categories = get_object_or_404(Category, slug=category_slug)
    products = get_object_or_404(Product, category__slug=category_slug, slug=prod_slug)
    colors = Color.objects.all()
    # categories = get_object_or_404(Category, slug=category_slug)
    # categories = Category.objects.get()
    # categories_slug = categories.slug
    context = {
        'products': products,
        'category': category,
        'categories': categories,
        'colors': colors

    }
    return render(request, 'shop/one-item.html', context)


def add_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            category = form.cleaned_data['category']
            new_category = form.cleaned_data['new_category']
            if new_category:
                category, created = Category.objects.get_or_create(name=new_category)
                if not created:
                    form.add_error('new_category', 'Такая категория уже существует')
            prod = Product(
                title=form.cleaned_data['title'],
                category=category,
                cover=form.cleaned_data['cover'],
                price=form.cleaned_data['price'],
                discount_price=form.cleaned_data['discount_price'],
                # size=form.cleaned_data['size'],
                # color=form.cleaned_data['color'],
            )
            prod.save()
            prod.size.set(form.cleaned_data['size'])
            prod.color.set(form.cleaned_data['color'])
            prod.save()
            return HttpResponseRedirect(reverse('edit-product', args=[prod.slug]))

    else:
        form = ProductForm()

    return render(request, 'shop/add-product.html', {'form': form, 'categories': categories})


def edit_product(request, prod_slug):
    product = get_object_or_404(Product, slug=prod_slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/shop/success')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/edit-product.html', context={'product': product, 'form': form}, )


# return render(request, 'feedback/feedback.html', context={'got_error': True})

def success(request):
    return render(request, 'shop/product-success.html')

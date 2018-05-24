from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Product, Category
from AbritesTask.helpers import pagination


def products(request):
    products = Product.objects.all()
    all_categories = Category.objects.all()
    pages = pagination(request, products, 10)

    context = {
        'all_categories': all_categories,
        'items': pages[0],
        'page_range': pages[1]
    }

    return render(request, 'index.html', context)


def products_by_category(request, pk):
    selected_category = Category.objects.get(id=pk)
    products = Product.objects.filter(category=selected_category)
    pages = pagination(request, products, 10)

    context = {
        'items': pages[0],
        'page_range': pages[1],
        'category': selected_category
    }

    return render(request, 'products_by_category.html', context)

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import DetailView

from .models import Product, Category
from AbritesTask.helpers import pagination
from cart.models import Cart


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

def products_by_name(request):
    products = Product.objects.all().order_by('name')
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
    all_categories = Category.objects.all()
    pages = pagination(request, products, 10)

    context = {
        'all_categories': all_categories,
        'items': pages[0],
        'page_range': pages[1],
        'category': selected_category
    }

    return render(request, 'products_by_category.html', context)


def products_in_cat_by_name(request, pk):
    selected_category = Category.objects.get(id=pk)
    products = Product.objects.filter(category=selected_category).order_by('name')
    all_categories = Category.objects.all()
    pages = pagination(request, products, 10)

    context = {
        'all_categories': all_categories,
        'items': pages[0],
        'page_range': pages[1],
        'category': selected_category
    }

    return render(request, 'products_by_category.html', context)


class ProductDetailView(DetailView):
    # model = Product
    template_name = 'product_detail.html'
    # context_object_name = 'product'

    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self):
        return get_object_or_404(Product, pk = self.kwargs['pk'])



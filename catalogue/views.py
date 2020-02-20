import copy

from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Category

# Create your views here.


def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }

    return render(request, "index.html", context)


def single_category(request, cat_id):
    category = get_object_or_404(Category, pk=cat_id)
    context = {
        "category": category
    }

    return render(request, "equipment.html", context)

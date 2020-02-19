from django.shortcuts import render,get_object_or_404
from django.views import generic

from .models import Category

# Create your views here.
def index(request):
  categories = Category.objects.all()
  context = {
    'categories':categories
  }

  return render(request, "index.html", context)
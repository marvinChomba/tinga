from django.contrib import admin

from .models import Category, Equipment, Images

# Register your models here.
admin.site.register(Category)
admin.site.register(Equipment)
admin.site.register(Images)

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("category/<int:cat_id>", views.single_category, name="single_cat")
]

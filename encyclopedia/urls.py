from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("w/search/", views.search, name="search"),
    path("w/create/", views.create, name="create"),
    path("w/save/", views.save, name="save"),
    path("w/edit/<str:title>", views.edit, name="edit"),
    path("w/update/<str:title>", views.update, name="update"),
    path("w/random", views.random, name="random")
]

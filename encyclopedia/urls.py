from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_name>", views.entry, name="wiki_entry"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("random", views.rand, name="random"),
    path("edit/<str:title>", views.edit, name="edit"),  
]

    # path("save_edit", views.save_edit, name="save_edit"),
    # path("save", views.save, name="save"),
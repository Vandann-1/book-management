from django.contrib import admin
from django.urls import path , include
from bookapp.views import *

urlpatterns = [
    # path("",homepage, name="homepage"),
    path("", book_list, name="book_list"),
    path("books/<int:pk>/", book_detail, name="book_detail"),
    path("books/create/", book_create, name="book_create"),
    path("books/<int:pk>/update/", book_update, name="book_update"),
    path("books/<int:pk>/delete/", book_delete, name="book_delete"),
    
]
from django.shortcuts import render

from .models import Books
from django.views.generic import ListView

# Create your views here.

class BooksView(ListView):
    template_name = 'main/list.html'
    queryset = Books.objects.all()
    context_object_name = 'books'



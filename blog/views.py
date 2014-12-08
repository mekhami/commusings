from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Article

# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'articles'
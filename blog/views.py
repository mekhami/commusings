from django.shortcuts import render
from django.views.generic import ListView, DetailView, View, FormView
from blog.models import Article, Comment
from blog.forms import CommentForm
from django.core.urlresolvers import reverse
from django.views.generic.detail import SingleObjectMixin



# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'articles'
    queryset = Article.objects.order_by("-pub_date")

class ArticleDisplay(DetailView):
    template_name = 'article.html'
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['form'] = CommentForm
        return context

class ArticleComment(SingleObjectMixin, FormView):
    form_class = CommentForm
    template_name = 'article.html'
    model = Article

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CommentView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('article-view', kwargs={'pk': self.object.pk})

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        view = ArticleDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ArticleComment.as_view()
        return view(request, *args, **kwargs)


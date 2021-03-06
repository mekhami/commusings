from django.views.generic import ListView, DetailView, View, CreateView
from blog.models import Article, Comment
from blog.forms import CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse


# Create your views here.
class IndexView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    queryset = Article.objects.order_by("-pub_date")
    paginate_by = 7

class ArticleDisplay(DetailView):
    template_name = 'blog/article.html'
    model = Article
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleDisplay, self).get_context_data(**kwargs)
        context['form'] = CommentForm
        return context

class CreateCommentView(CreateView):
    model = Comment
    template_name = 'blog/article.html'
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        self.article = get_object_or_404(Article, slug=kwargs['slug'])
        return super(CreateCommentView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super(CreateCommentView, self).get_context_data(article=self.article, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.article
        comment.save()
        return redirect('article-view', slug=comment.article.slug)

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        view = ArticleDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CreateCommentView.as_view()
        return view(request, *args, **kwargs)


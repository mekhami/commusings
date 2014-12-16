from django.conf.urls import url, patterns

from .views import IndexView, ArticleView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^article/(?P<slug>[-\w]+)/$', ArticleView.as_view(), name='article-view'),
)
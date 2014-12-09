from django.conf.urls import url, patterns

from .views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[-_\w]+)/$', ArticleView.as_view(), name='article'),
)
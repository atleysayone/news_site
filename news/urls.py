from django.conf.urls import url, include

from news import views
from news.views import NewsListView, NewsDetailView, search, NewsCatView, ajax_title_search, search123, \
    ajax_title_search2

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news-list'),
    url(r'^(?P<newstype>\w+)/(?P<slug>[\w-]+)$',NewsDetailView.as_view(), name='news-details'),
    url(r'^new$',views.search),
    url(r'^(?P<newstype>\w+)$',NewsCatView.as_view(), name='news-cat-view'),
    url(r'^search/$', ajax_title_search, name='demo_title_search'),
    url(r'^search2/$', ajax_title_search2, name='demo_title_search2'),
    url(r'^list/$', search123, name='news-list1'),
    url(r'^comments/', include('django_comments.urls')),

]


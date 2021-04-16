from django.conf.urls import url
from . import views

###配置路由
app_name = 'blog'#开头 防止重名

urlpatterns = [

    url(r'^$',views.index, name='blog_index'),#https://127.0.0.1/blog/
    url(r'^(?P<blog_id>[0-9]+)/$', views.detail, name='blog_detail'),#正则表达式
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='blog_category'),#/category/3/  分类视图
    url(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]+)$', views.archives, name='blog_archives'),
    url(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag, name='blog_tag'),  # /category/3/  分类视图
    url(r'^search/$', views.search, name='blog_search'),  #
    url(r'^reply/(?P<comment_id>\d+)/$', views.reply, name='comment_reply'),
]

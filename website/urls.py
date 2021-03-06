"""website URL Configuration
###根路由
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from blog.feed import LatestEntriesFeed
from blog import views as blog_views
#导入sitemap
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Entry

info_dict = {#字典

    'queryset':Entry.objects.all(),

    'date_field':'modified_time'

}


urlpatterns = [

    url(r'^$',blog_views.index),

    url(r'^admin/', admin.site.urls),

    url(r'^blog/', include('blog.urls')),

    url(r'^login/$', blog_views.login),

    url(r'^logout/$', blog_views.logout),

    url(r'^latest/feed/$', LatestEntriesFeed()),

    url(r'^comments/', include('django_comments.urls')),

    url(r'^sitemap\.xml$',sitemap,{'sitemaps':{'blog':GenericSitemap(info_dict,priority=0.6)}},

        name='django.contrib.sitemaps.views.sitemap'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler403 = blog_views.permission_denied#403无权限访问

handler404 = blog_views.page_not_found#404

handler500 = blog_views.page_error#500服务器错误




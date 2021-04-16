#-*- coding = utf-8 -*-
#@time : 2021/4/13 20:50
#@author : xyF
#@file : feed.py
#@software : PyCharm

##RSS订阅
from django.contrib.syndication.views import Feed
# from django.urls import reverse
from .models import Entry


class LatestEntriesFeed(Feed):
    title = "我的博客网站"
    link = "/siteblogs/"
    description = "最新更新的博客文章！"

    def items(self):
        return Entry.objects.order_by('-created_time')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.abstract
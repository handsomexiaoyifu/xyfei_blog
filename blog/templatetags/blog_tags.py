#-*- coding = utf-8 -*-
#@time : 2021/4/13 16:39
#@author : xyF
#@file : blog_tags.py
#@software : PyCharm


###自定义模板标签
from django import template
from ..models import Entry,Category,Tag

register = template.Library()

@register.simple_tag
def get_recent_entries(num=5):#自定义获取最新博客
    return Entry.objects.all().order_by('-created_time')[:num]#切片

@register.simple_tag
def get_popular_entries(num=5):#自定义获取推荐博客
    return Entry.objects.all().order_by('-visiting')[:num]#切片

@register.simple_tag
def get_categories():#获取分类
    return Category.objects.all()

@register.simple_tag
def get_entry_count_of_category(category_name):
    return Entry.objects.filter(category__name=category_name).count()

@register.simple_tag
def archives():
    return Entry.objects.dates('created_time','month',order='DESC')


@register.simple_tag
def get_entry_count_of_date(year,month):
    return Entry.objects.filter(created_time__year=year,created_time__month=month).count()

@register.simple_tag
def get_tags():
    return Tag.objects.all()



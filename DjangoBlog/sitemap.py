#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.net/
@software: PyCharm
@file: sitemap.py
@time: 2016/12/15 下午10:26
"""

from django.contrib.sitemaps import Sitemap
from blog.models import Article, Category, Tag
from accounts.models import BlogUser
from django.contrib.sitemaps import GenericSitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):            #不希望在站点地图中出现一些静态页面，比如商品的详细信息页面
        return ['blog:index', ] #显式列出这些页面的网址名称，并在网站地图的location方法中调用reverse()

    def location(self, item):
        return reverse(item) #显式列出这些页面的网址名称，并在网站地图的location方法中调用reverse()


class ArticleSiteMap(Sitemap):
    changefreq = "monthly"
    priority = "0.6"

    def items(self):
        return Article.objects.filter(status='p')

    def lastmod(self, obj):
        return obj.last_mod_time


class CategorySiteMap(Sitemap):
    changefreq = "Weekly"
    priority = "0.6"

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.last_mod_time


class TagSiteMap(Sitemap):
    changefreq = "Weekly"
    priority = "0.3"

    def items(self):
        return Tag.objects.all()

    def lastmod(self, obj):
        return obj.last_mod_time


class UserSiteMap(Sitemap):
    changefreq = "Weekly"
    priority = "0.3"

    def items(self):
        return list(set(map(lambda x: x.author, Article.objects.all())))

    def lastmod(self, obj):
        return obj.date_joined

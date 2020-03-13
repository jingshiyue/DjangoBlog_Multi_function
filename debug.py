import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","DjangoBlog.settings")
import django,time
django.setup()
from django.core.cache import cache
from django.core.cache import caches
from django.utils.cache import get_cache_key
from DjangoBlog.utils import get_current_site
from django.contrib.sites.models import Site

# s = Site.objects.filter().update(domain="example1.com")
# print(s)
# site = get_current_site().domain
# print(":::::::::::::::::::::",site)
# site = Site.objects.get_current()
# print(site)
# from DjangoBlog.utils import *
# send_email(["173302591@qq.com"],
#             "测试邮件title",
#             "邮件内容++++++++++"
# )
from oauth.models import *
t = OAuthUser().__class__
print(t)
print("####################################")



cache.set('my_key1', 'hello, world!',60*60*12)
cache.set('my_key2', 'hello, world!', 60)
cache.set('my_key3', 'hello, world!', 60)

# t = cache.get('my_key2')  #只取了缓存表里的key， 前缀:版本 都没有取
# print(t)
# print("timeout...")
# time.sleep(3)
# t = cache.get('my_key2')
# print(t)
print(cache)
print(caches["locmemcache"])
from django.core.cache.utils import make_template_fragment_key


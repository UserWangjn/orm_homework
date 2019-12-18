#coding=utf-8
#@Author:Administrator
#@date:2019/12/9   18:11

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm_homework.settings')

import django
django.setup()

from app01 import models
from django.db.models import Avg,Sum,Max,Min,Count

# https://www.cnblogs.com/maple-shaw/articles/9414626.html
# 查找所有书名里包含金老板的书
ret = models.Book.objects.filter(title__contains='金老板')
# print(ret)
# for i in ret:
#     name = i.title
#     print(name)
# 查找出版日期是2018年的书
ret = models.Book.objects.filter(publish_date__year='2018')
# print(ret)
# 查找出版日期是2017年的书名
ret = models.Book.objects.filter(publish_date__year='2017')
# for i in ret:
#     print(i.title)
# 查找价格大于10元的书
ret = models.Book.objects.filter(price__gt=10)
# print(ret)
# 查找价格大于10元的书名和价格
ret = models.Book.objects.filter(price__gt=10)
# for i in ret:
#     print('书名：{0}，价格：{1}'.format(i.title,i.price))
# 查找memo字段是空的书
ret = models.Book.objects.filter(memo__isnull=True)
# print(ret)
# 查找在北京的出版社
ret = models.Publisher.objects.filter(city='北京')
# print(ret)
# 查找名字以沙河开头的出版社
ret = models.Publisher.objects.filter(name__startswith='沙河')
# print(ret)
# 查找“沙河出版社”出版的所有书籍
ret = models.Book.objects.filter(publisher__name='沙河出版社')
# publisher_obj = models.Publisher.objects.filter(name='沙河出版社')
# publisher_obj = models.Publisher.objects.first()
# books = publisher_obj.book_set.all()
# print(books)
# print(ret)
# 查找每个出版社出版价格最高的书籍价格
# ret = models.Book.objects.values('publisher_id').annotate(max_price=Max('price')).values('max_price','publisher_id')
ret = models.Publisher.objects.annotate(Max('book__price')).values()
# print(ret)
# 查找每个出版社的名字以及出的书籍数量
# 分组：annotate
# 聚合：aggregate
ret = models.Publisher.objects.annotate(book_count=Count('book__id')).values('book_count','name')
# print(ret)
# 查找作者名字里面带“小”字的作者
ret = models.Author.objects.filter(name__contains='小')
# print(ret)
# 查找年龄大于30岁的作者
ret = models.Author.objects.filter(age__gt=30)
# print(ret)
# 查找手机号是155开头的作者
ret = models.Author.objects.filter(phone__startswith='155')
# print(ret)
# 查找手机号是155开头的作者的姓名和年龄
ret = models.Author.objects.filter(phone__startswith='155').values('name','age')
# print(ret)
# 查找每个作者写的价格最高的书籍价格
# ret = models.Book.objects.values('author__id').annotate(max_price=Max('price')).values('author__id','author__name','max_price')
ret = models.Author.objects.annotate(Max('book__price')).values()
# print(ret)
# 查找每个作者的姓名以及出的书籍数量
ret = models.Author.objects.annotate(book_count=Count('book__id')).values('name','book_count')
# print(ret)
# 查找书名是“跟金老板学开车”的书的出版社
ret = models.Publisher.objects.filter(book__title='跟金老板学开车')
# print(ret)
# 查找书名是“跟金老板学开车”的书的出版社所在的城市
ret = models.Publisher.objects.filter(book__title='跟金老板学开车').values('city')
# print(ret)
# 查找书名是“跟金老板学开车”的书的出版社的名称
ret = models.Publisher.objects.filter(book__title='跟金老板学开车').values('name')
# print(ret)
# 查找书名是“跟金老板学开车”的书的出版社出版的其他书籍的名字和价格
pulisher_obj = models.Publisher.objects.get(book__title='跟金老板学开车')
ret = pulisher_obj.book_set.exclude(title='跟金老板学开车').values('title','price')
# print(ret)
# 查找书名是“跟金老板学开车”的书的所有作者
ret = models.Author.objects.filter(book__title='跟金老板学开车')
# print(ret)
# 查找书名是“跟金老板学开车”的书的作者的年龄
ret = models.Author.objects.filter(book__title='跟金老板学开车').values('name','age')
# print(ret)
# 查找书名是“跟金老板学开车”的书的作者的手机号码
ret = models.Author.objects.filter(book__title='跟金老板学开车').values('name','phone')
# print(ret)
# 查找书名是“跟金老板学开车”的书的作者们的姓名以及出版的所有书籍名称和价钱
author_objs = models.Author.objects.filter(book__title='跟金老板学开车')
for i in author_objs:
    ret = i.book_set.values('author__name','title','price')
    # print(ret)

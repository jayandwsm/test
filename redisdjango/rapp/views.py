import datetime
import json

from django.shortcuts import render

from django.conf import settings
from django.core.cache import cache
from django.views.decorators.cache import cache_page

# Create your views here.
from rapp.models import Publisher, Book, Author


def set_redis(request):
    key = "jay"
    cache.set(key,json.dumps("123"),settings.NEVER_REDIS_TIMEOUT)
    return render(request,"show.html")

def read_redis(request):
    key = "jay"
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data  = json.loads(value)
    return render(request, "show.html",{"data":data})

@cache_page(10)
def p(request):
    print('@@@@@@@@@@@@')
    return render(request,"show.html")

def insert_object(request):
    # p1 = Publisher(name='Apress',
    #                address='2855 Telegraph Avenue',
    #                city = 'Berkeley',
    #                state_province = 'CA',
    #                country = 'U.S.A.',
    #                website = 'http://www.apress.com/')
    # p1.save()
    # p2 = Publisher(name="O'Reilly",
    #                address='10 Fawcett St.',
    #                city = 'Cambridge',
    #                state_province = 'MA',
    #                country = 'U.S.A.',
    #                website = 'http://www.oreilly.com/')
    # p2.save()
    #
    # a1 = Author.objects.create(first_name ="jay",
    #             last_name = 'jay',
    #             email = 'jay@163.com')
    # a2 = Author.objects.create(first_name="wsm",
    #             last_name='wsm',
    #             email='wsm@163.com')
    # a3 = Author.objects.create(first_name="zxc",
    #             last_name='zxc',
    #             email='zxc@163.com')

    # b1 = Book.objects.create(title="book1",
    #                          authors="jay",
    #                          publisher="O'Reilly",
    #                          publication_date=datetime.datetime.now())
    # b2 = Book.objects.create(title="book1",
    #                          authors="wsm",
    #                          publisher="O'Reilly",
    #                          publication_date=datetime.datetime.now())
    # b3 = Book.objects.create(title="book2",
    #                          authors="jay",
    #                          publisher="Apress",
    #                          publication_date=datetime.datetime.now())
    # b4 = Book.objects.create(title="book2",
    #                          authors="wsm",
    #                          publisher="Apress",
    #                          publication_date=datetime.datetime.now())
    # b5 = Book.objects.create(title="book3",
    #                          authors="zxc",
    #                          publisher="Apress",
    #                          publication_date=datetime.datetime.now())
    # b6 = Book.objects.create(title="book4",
    #                          authors="zxc",
    #                          publisher="O'Reilly",
    #                          publication_date=datetime.datetime.now())
    # print("查询这个出版社所有书")
    # p1 = Publisher.objects.filter(name='Apress')
    # all_book = p1[0].book_set.all()
    # print(all_book)
    # p1 = Book.objects.filter(publisher_id = 7)
    # print(p1)
    print("查询这本书的所有作者")
    # b1 = Book.objects.filter(title="book2")
    # print(b1)
    # a1 = b1
    # print(a1)
    print("正向查询")
    b1 = Book.objects.get(title="book2")
    all_author = b1.authors.all()
    print(all_author)
    print("查询这个作者的所有书")
    print("反向查询")
    author = Author.objects.get(first_name ="jay")
    all_book = author.book_set.all()
    print(all_book)
    # # a1 = Author.objects.
    # print("查询这个作者的所有书")
    # b1 = Book.objects.filter(authors="zxc")
    # print(b1)
    # a1 = Book.objects.filter(authors="zxc")
    # b1 = a1[0].book_all()
    # print(b1)
    return render(request,"show.html",locals())












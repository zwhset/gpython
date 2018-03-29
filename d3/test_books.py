# -*- coding: utf-8 -*-

"""
    package.module
    ~~~~~~~~~~~~~~

    Test books

    :copyright: (c) YEAR by zwhset.
    :license: GOMEOPS, see LICENSE_FILE for more details.
"""

import requests
import urlparse

base_url = 'http://localhost:8000/'

def test_books():
    """测试所有的books"""
    resource = '/api/books'
    url = urlparse.urljoin(base_url, resource)
    r = requests.get(url)
    try:
        books = r.json()

        # 测试所有书的标题
        for book in books:
            if not book.get('title', None):
                print 'test_books book title None', book.get('id', 0)

        # 完成测试
        print 'test_books: test all book OK...'

    except:
        print 'test_books result not json'


def test_book():
    """测试一本书"""
    ids = ['1', 'a', '99', 'asdfasdfwerqweradsfadf', 'asasdffd231', 1, 2, 99]

    for id in ids:
        resource = '/api/book/{id}'.format(id=id)
        url = urlparse.urljoin(base_url, resource)
        r = requests.get(url)
        try:
            book = r.json()
            # 测试书的标题
            if book.get('code', 0):
                if not book.get('title', None):
                    print 'test_book: url:{url} error id={id}'.format(url=url, id=book.get('id', 0))
        except:
            print 'test_book: {url} not json'.format(url=url)

    # 完成测试
    print 'test_book: test a book OK...'

def create_book():
    """创建一本书"""
    pass

def delete_book():
    """删除一本书"""
    pass

def update_book():
    pass

test_books()
test_book()
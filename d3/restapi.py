# -*- coding: utf-8 -*-

# 作者： 煮酒品茶

"""
    package.module
    ~~~~~~~~~~~~~~

    python实现的图书的一个restful api.

    参考restful设计指南 URL：
        http://www.ruanyifeng.com/blog/2014/05/restful_api.html

    restful api 一般模式：
        GET（SELECT）：从服务器取出资源（一项或多项）。
        POST（CREATE）：在服务器新建一个资源。
        PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
        PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。
        DELETE（DELETE）：从服务器删除资源。

    注意：
       没有做存储持久化，为了实现例子，实际上应该是从数据库里面拿，而增册改查方法也应该调用
       后端的方法。

    :copyright: (c) YEAR by zwhset.
    :license: GOMEOPS, see LICENSE_FILE for more details.
"""

from flask import Flask, request, jsonify
import random

app = Flask(__name__)

books = [
    dict(id=1, isdn=random.randrange(1, 1000), title='a python book', author=dict(
        name='l0set', city='hunan'
    )),
    dict(id=2, isdn=random.randrange(1, 1000), title='a golang book', author=dict(
        name='zwhset', city='beijing'
    ))
]

# error action
@app.errorhandler(405)
def page_not_found(e):
    return jsonify(dict(code=1, message='method error.')), 405

# get all books
@app.route('/api/books')
def handle_books():
    return jsonify(books)

# get a book
@app.route('/api/book/<int:id>')
def handle_book(id):
    for i, book in enumerate(books):
        if book['id'] == id:
            return jsonify(book)
    return jsonify(dict(code=2, message="don't fund the book"))

# create a new book
@app.route('/api/book', methods=['POST'])
def create_book():
    book = request.json
    print book, type(book)

    # check params
    if  ((not 'title' in book and 'author' in book) or
        (not isinstance(book['author'], dict)) or
        (not 'name' in book['author'] and 'city' in book['author'])):
        return jsonify(code=3, message='json author error.')

    # create a new book
    book['id'] = random.randrange(1, 10000)
    book['isdn'] = random.randrange(1, 10000)
    books.append(book)
    return jsonify(code=0, message='success')

# update book
@app.route('/api/book/<int:id>', methods=['PUT'])
def update_book(id):
    book = request.json

    # check params
    if ((not 'title' in book and 'author' in book) or
            (not isinstance(book['author'], dict)) or
            (not 'name' in book['author'] and 'city' in book['author'])):
        return jsonify(code=3, message='json author error.')

    # 安全考虑，只拿要的数据，其它的不要
    book_data = dict(title=book['title'],
                     author=dict(
                         name=book['author']['name'],
                         city=book['author']['city']
                     ))

    for i, book in enumerate(books):
        # check id
        if book['id'] == id:
            books[i].update(book_data) # 进行更新操作
            return jsonify(code=0, message='success')

    return jsonify(dict(code=2, message="don't fund the book"))

# delete a book
@app.route('/api/book/<int:id>', methods=['DELETE'])
def delete_book(id):
    for i, book in enumerate(books):
        # check id
        if book['id'] == id:
            del books[i] # 删除书
            return jsonify(code=0, message='success')

    return jsonify(dict(code=2, message="don't fund the book"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
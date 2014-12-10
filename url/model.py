from hashlib import sha1

from flask import request

def insert(content):
    args = (content, None)
    (_, id) = request.cur.callproc('url_insert', args)
    return id

def get_digest(content):
    args = (sha1(content).digest(), None)
    (_, id) = request.cur.callproc('url_get_digest', args)
    return id

def get_content(id):
    args = (id, None)
    (_, content) = request.cur.callproc('url_get_content', args)
    return content
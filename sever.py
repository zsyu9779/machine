#!/usr/bin/env python
# coding=utf-8

import socket
import re

HOST = '127.0.0.1'
PORT = 8888

# Read index.html, put into HTTP response data
index_content = '''
HTTP/1.x 200 ok
Content-Type: text/html

'''

file = open('index.html', 'r')
index_content += file.read()
file.close()

# Read reg.html, put into HTTP response data
reg_content = '''
HTTP/1.x 200 ok
Content-Type: text/html

'''

# file = open('reg.html', 'r')
# reg_content += file.read()
# file.close()

# # Read picture, put into HTTP response data
# file = open('T-mac.jpg', 'rb')
# pic_content = '''
# HTTP/1.x 200 ok
# Content-Type: image/jpg
#
# '''
# pic_content += file.read()
# file.close()

# Configure socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(100)

# infinite loop
while True:
    # maximum number of requests waiting
    conn, addr = sock.accept()
    request = conn.recv(1024)
    print(request)
    method = request.split(' '.encode(encoding="utf-8"))[0]
    src = request.split(' '.encode(encoding="utf-8"))[1]

    print
    'Connect by: ', addr
    print
    'Request is:\n', request

    # deal wiht GET method
    if method == "b'GET":
        if src == '/index.html':
            content = index_content
        elif src == '/T-mac.jpg':
            content = pic_content
        elif src == '/reg.html':
            content = reg_content
        elif re.match('^/\?.*$', src):
            entry = src.split('?')[1]  # main content of the request
            content = 'HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'
            content += entry
            content += '<br /><font color="green" size="7">register successs!</p>'
        else:
            continue


    # deal with POST method
    elif method == 'POST':
        form = request.split('\r\n')
        entry = form[-1]  # main content of the request
        content = 'HTTP/1.x 200 ok\r\nContent-Type: text/html\r\n\r\n'
        content += entry
        content += '<br /><font color="green" size="7">register successs!</p>'

    ######
    # More operations, such as put the form into database
    # ...
    ######

    else:
        continue

    conn.sendall(content)

    # close connection
    conn.close()
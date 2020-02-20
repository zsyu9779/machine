import socket
import json
import Handling_color_blocks
import threading
HOST = '127.0.0.1'
PORT = 1234
web = socket.socket()
web.bind((HOST,PORT))

web.listen(5)
print('sever is listening...')

while True:
    client_connection,client_address = web.accept()  #建立客户端连接
    print('link addr:')
    print(client_address)
    client_connection.send(str.encode("HELLO,WORLD"))
    data = client_connection.recv(1024)
    print(type(data))
    result = str(data, encoding='utf-8')
    json1 = json.loads(result)
    Handling_color_blocks.move_blocks(json1)
    print(json)


client_connection.close()
import socket

HOST = '127.0.0.1'     #获取本地主机名
PORT = 1234                #设置端口号
ADDR = (HOST,PORT)

web = socket.socket()

web.connect(ADDR)
data = '''{
    "x_pic": 200,
    "y_pic": 100,
    "angle": 10,
    "field": "red"
}'''
#请求与服务器建立连接
web.send(str.encode(data))   #向服务器发送信息

data = web.recv(1024)       #接收数据
print(data)


web.close()

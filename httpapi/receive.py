import socket
import json

ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ListenSocket.bind(('localhost', 5701))
ListenSocket.listen(100)

HttpResponseHeader = '''HTTP/1.1 200 OK
Content-Type: text/html
'''

def request_to_json(msg):
    for i in range(len(msg)):
        if msg[i]=="{" and msg[-1]=="}":
            return json.loads(msg[i:])
    return None

#需要循环执行，返回值为json格式
def rev_msg():# json or None
    Client, Address = ListenSocket.accept()
    Request = Client.recv(1024).decode(encoding='utf-8')
    #print(Request)
    rev_json=request_to_json(Request)
    Client.sendall((HttpResponseHeader).encode(encoding='utf-8'))
    Client.close()
    return rev_json

#https://juejin.im/entry/5af5453c518825427064051c

'''
POST / HTTP/1.1     
Host: 127.0.0.1:5701
Accept: */*
Content-Type: application/json; charset=UTF-8
User-Agent: CQHttp/4.15.0
X-Self-ID: 2821876761
Content-Length: 442

{"anonymous":null,"font":44647336,"group_id":814844378,"message":[{"data":{"text":"来"},"type":"text"}],"message_id":4430,"message_type":"group","post_type":"message","raw_message":"来","self_id":2821876761,"sender":{"age":29,"area":"爱尔兰","card":"Web划水级选手","level":"话唠","nickname":"wh1sper低语","role":"admin","sex":"male","title":"Web","user_id":1643239341},"sub_type":"normal","time":1594221754,"user_id":1643239341}
'''
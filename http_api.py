import socket
import requests
import json

"""

Usage::
  >>> from HttpAPI import *

"""


listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind(('localhost', 5701))
listen_socket.listen(100)

http_response_header = '''HTTP/1.1 200 OK
Content-Type: text/html

'''


def receive_message():
    ''' 需要循环执行，return json/None
    Usage::
      >>> while True:
      >>>   receive_message()

    # https://juejin.im/entry/5af5453c518825427064051c
    '''
    _client, _address = listen_socket.accept()
    _request = _client.recv(1024).decode(encoding='utf-8')
    _client.sendall(http_response_header.encode())
    _client.close()
    i, j = 0, len(_request)-1
    while i < j and _request[i] != "{": i += 1
    while i < j and _request[j] != "}": j -= 1
    
    if i >= j: return False # 不存在json
    
    JSON = _request[i:j+1]
    # heartbeat
    if JSON.startswith('{"interval":5000'): return False
    
    JSON = json.loads(JSON)
    print(JSON)
    if JSON['post_type'] == 'request' and JSON['request_type'] == 'friend':
        set_friend_add_request(JSON['flag'])
        return False
    return JSON

def send_msg(msg, tar_id, tar_obj):
    ''' 调用此函数来进行一条消息的发送
    :param msg:     (str), 发送的内容
    :param tar_id:  (int), QQ号/群号
    :param tar_obj: (str), "private", "group"

    Usage::
      >>> send_msg("hello world", 1175078221, "private")
    '''
    
    if tar_obj == "private":
        api_url = "http://127.0.0.1:5700/send_private_msg"
        r = requests.post(api_url, data={"user_id": tar_id, "message": msg, "auto_escape": False}, timeout=3)
    elif tar_obj == "group":
        api_url = "http://127.0.0.1:5700/send_group_msg"
        r = requests.post(api_url, data={"group_id": tar_id, "message": msg, "auto_escape": False}, timeout=3)
    else:
        return False
    print("[+]73:", r.json())
    if r.text[-4:-2] == "ok":
        return True
    return False

def set_friend_add_request(flag):
    '''好友请求'''
    api_url = "http://127.0.0.1:5700/set_friend_add_request"
    r = requests.post(api_url, data={"flag":flag, "approve":True, "remark":""})


def set_group_kick(group_id, user_id):
    ''' group_id:"int", 群组号
        user_id:"int", QQ号
    '''
    api_url = "http://127.0.0.1:5700/set_group_kick"
    r = requests.post(api_url, data={
                      "group_id": group_id, "user_id": user_id, "reject_add_request": False})


def set_group_ban(group_id, user_id, ban_time=60):
    ''' group_id: "int", 群组号
        user_id: "int", QQ号
        ban_time: "int", 禁言时间(s)
    '''
    api_url = "http://127.0.0.1:5700/set_group_ban"
    r = requests.post(
        api_url, data={'group_id': group_id, 'user_id': user_id, 'duration': ban_time})


def set_group_card(group_id, user_id, card):
    ''' group_id: "int",群组号
        user_id: "int",QQ号
        card: "str",成员备注
    '''
    api_url = 'http://127.0.0.1:5700/set_group_card'
    r = requests.post(
        api_url, data={"group_id": group_id, "user_id": user_id, "card": card})


def get_stranger_info(user_id):
    '''
    Usage:
      >>> print(get_stranger_info(1175078221))
    '''
    api_url = 'http://127.0.0.1:5700/get_stranger_info'
    try:
        r = requests.post(
            api_url, data={'user_id': user_id, 'no_cache': False})
        return r.json()["data"]["nickname"]
    except:
        return None


def send_like(user_id, times=10):

    api_url = 'http://127.0.0.1:5700/send_like'
    try:
        r = requests.post(api_url, data={"user_id": user_id, "times": times})
        return True
    except:
        return None


def get_image(file):  # 未测试~~~
    '''
    file: "str", CQ:file参数,6B4DE3DFD1BD271E3297859D41C530F5.jpg
    '''
    api_url = 'http://127.0.0.1:5700/get_image'
    r = requests.post(api_url, data={'file': file})
    return r.text


def can_send_image():
    '''测试能否发送图片 (return True/False/None)'''
    api_url = 'http://127.0.0.1:5700/can_send_image'
    r = requests.post(api_url)
    try:
        return json.loads(r.text)["data"]["yes"]
    except:
        return None

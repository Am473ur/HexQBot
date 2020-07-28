import requests
import json

def get_stranger_info(user_id):
    data = {
            'user_id':user_id,
            'no_cache':False
    }
    api_url = 'http://127.0.0.1:5700/get_stranger_info'
    try:
        r = requests.post(api_url,data=data)
        print(r.json())
        return r.json()["data"]["nickname"]
    except:
        return None

#print(get_stranger_info(123))
def send_like(user_id,times=10):
    data = {
            'user_id':user_id,
            'times':times
    }
    api_url = 'http://127.0.0.1:5700/send_like'
    try:
        r = requests.post(api_url,data=data)
        return True
    except:
        return None
def get_image(file):#未测试~~~
    '''返回图片链接:C:\app\CoolQ\data\image\6B4DE3DFD1BD271E3297859D41C530F5.jpg
    file:"str",CQ:file参数,6B4DE3DFD1BD271E3297859D41C530F5.jpg
    '''
    data = {'file':file}
    api_url = 'http://127.0.0.1:5700/get_image'
    r = requests.post(api_url,data=data)
    return r.text

def can_send_image():
    '''测试能否发送图片(bool)'''
    api_url = 'http://127.0.0.1:5700/can_send_image'
    r = requests.post(api_url)
    try:
        bool_ans=json.loads(r.text)["data"]["yes"]
        return bool_ans
    except:
        return None




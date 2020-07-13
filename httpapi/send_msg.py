import requests

def send_msg(msg,tar_id,tar_obj):#print
    '''调用此函数来进行一条消息的发送\n
    msg："str",发送的内容\n
    tar_id："int",QQ号/群号/讨论组号\n
    tar_obj:"str",选择发送的对象,"private","group","discuss"
    '''
    if tar_obj == "private":
        data = {
            'user_id':tar_id,
            'message':msg,
            'auto_escape':False
        }
        api_url = 'http://127.0.0.1:5700/send_private_msg'
        r = requests.post(api_url,data=data)
    elif tar_obj=="group":
        data = {
            'group_id':tar_id,
            'message':msg,
            'auto_escape':False
        }
        api_url = 'http://127.0.0.1:5700/send_group_msg'
        r = requests.post(api_url,data=data)
    elif tar_obj=="discuss":
        data = {
            'discuss_id':tar_id,
            'message':msg,
            'auto_escape':False
        }
        api_url = 'http://127.0.0.1:5700/send_discuss_msg'
        r = requests.post(api_url,data=data)
    else:
        return False
    if r.text[-4:-2]=="ok":
        return True
    return False

#send_msg("test",1175078221,tar_obj="private")
#print(send_msg("8909",1175078221,tar_obj="private"))

'''
[CQ:shake] 戳一戳,仅支持好友消息
[CQ:at,qq={1}] {1} 被@的群成员帐号。若该参数为all，则@全体成员（次数用尽或权限不足则会转换为文本）。
[CQ:image,file={1}] {1} 图片文件名称，图片存放在酷Q目录的data\image\下
'''
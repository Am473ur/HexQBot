import json
import base64
import requests
import re
from BaiduImg import *

header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
}
self_qq = json.load(open("config.json"))["self_qq"]

def split_msg_img(rev):
    msg = rev["raw_message"].replace("[CQ:at,qq={}]".format(self_qq), "").replace(" ", "").replace("\n","")  # 私聊还@Hex？发空格？爪巴~直接过滤~
    if "[CQ:image,file=" not in msg:
        return [None, msg]  # msg不含有图片
    if msg.count("[CQ:image,file=") > 1:  # 一次识别好几张图片？给爷爬
        return [False, "Hex酱一次只能看一张图片呀~"]
    img_url = rev["message"][rev["message"].find("url="):][4:-1]
    try:
        html = requests.get(img_url, headers=header)
        # "http:"开头的图片链接需要get下来然后转base64才能给百度AI识别
        img = base64.b64encode(html.content)
    except:
        # print('获取该图片失败')
        return [False, "Hex酱好像出现了点问题，图片没有下载成功啊~qaq"]
    msg = msg.replace(re.findall("\[CQ:image,file=[A-Za-z0-9\?.,=:/_-]*", msg)[0], "")
    # msg只含有一张图片(或还有一些文字) [文本，图片的base64]
    return [True, msg, img, img_url]

def reply(rev):
    msg_img = split_msg_img(rev)
    """ 图片下载出现问题 """
    if msg_img[0] == False: # 出错就返回报错内容
        return msg_img[1]
    """ handle picture """
    if msg_img[0] == None:
        return "不包含图片"
    if msg_img[0] == True:
        recv_handle_picture = handle_picture(msg_img[1], msg_img[2])
        return recv_handle_picture[1]

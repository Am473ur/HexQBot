from app.Baidu_image.temp_data.msg_data import *
from app.Baidu_image.ai_img_types import *
import json
import base64
import time
from random import choice

def get_date():
    temp=time.localtime()
    temp=[str(temp[i]) for i in range(3)]
    return "app/Baidu_image/temp_data/"+temp[0]+"_"+temp[1]+"_"+temp[2]+".txt"


def load_uesr_data():
    user_data=json.load(open("app/Baidu_image/temp_data/user_data.json","r"))
    return user_data


def can_upload_img(Qnum):
    pass

def img_recognizer(msg, img_b64, Qnum):#这是个不管什么情况，都需要返回字符串的函数
    if img_b64[:8]==b'R0lGODlh':#可以先判断一下图片格式，以防是百度AI不支持的格式
        return "Gif格式的图片我可看不懂呀"
    #if can_upload_img(Qnum): 占坑待填
    #    return "爬，你今天次数用完了，明天再来"
    for i in msg_to_img["animal"]:
        if i in msg:
            return img_animal(img_b64)
    for i in msg_to_img["plant"]:
        if i in msg:
            return img_plant(img_b64)
    for i in msg_to_img["logo"]:
        if i in msg:
            return img_logo(img_b64)
    for i in msg_to_img["ingredient"]:
        if i in msg:
            return img_ingredient(img_b64)
    for i in msg_to_img["dish"]:
        if i in msg:
            return img_dish(img_b64)
    for i in msg_to_img["redwine"]:
        if i in msg:
            return img_redwine(img_b64)
    for i in msg_to_img["currency"]:
        if i in msg:
            return img_currency(img_b64)
    for i in msg_to_img["landmark"]:
        if i in msg:
            return img_landmark(img_b64)
    for i in msg_to_img["car"]:
        if i in msg:
            return img_car(img_b64)
    return img_advanced_general(img_b64)



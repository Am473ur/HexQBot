import re
import base64
import requests
from httpapi.features import send_like
from app.Hex_talker.help_sys import help_menu
from app.HexCTF_afdian.post_cost import team_cost
from app.Hex_talker.smart_talking import s_talking
from app.GHS_pic.ghs_pic import hso_pic
from app.Baidu_image.img_ai import img_recognizer
from app.Run_code.runcode import rcode
from data.talk_data.deal_talk_data import *
from data.talk_data.base_talk import *
from httpapi.features import get_stranger_info
from random import choice
import json

# --------------------------------------------developer----------------------------------------------------


def save_main_conf(main_conf):
    open("conf/main_conf.json", "w").write(json.dumps(main_conf))


def get_admins(main_conf):
    will_send = "Admin List:\n"
    if len(main_conf["admin"]) == 0:
        return "There is no admin."
    for Qnum in main_conf["admin"]:
        nickname = get_stranger_info(Qnum)
        if nickname != None:
            will_send += nickname
        will_send += str(Qnum)+"\n"
    return will_send[:-1]  # 删去最后一个回车


def do_add_admin(Qnum, main_conf):
    if Qnum in main_conf["admin"]:
        return "This QQ is already an administrator."
    main_conf["admin"].append(Qnum)
    save_main_conf(main_conf)
    return "添加成功~{}成为管理员啦~".format(Qnum)


def do_del_admin(Qnum, main_conf):
    if Qnum not in main_conf["admin"]:
        return "This QQ is not an administrator."
    main_conf["admin"].remove(Qnum)
    save_main_conf(main_conf)
    return "移除成功~已将{}从管理员中移除啦~".format(Qnum)


def talk_to_developer(rev, main_conf):
    msg = rev["raw_message"]
    if msg[:6] == "admins":
        return get_admins(main_conf)
    if msg[:6] == "admin+":
        return do_add_admin(int(msg[6:]), main_conf)
    if msg[:6] == "admin-":
        return do_del_admin(int(msg[6:]), main_conf)
    return None


# --------------------------------------------admin----------------------------------------------------

def admin_add_data(msg, talk_data):
    try_add_data = add_data(msg, talk_data)
    if try_add_data == False:
        return False
    if try_add_data == True:
        return choice(right_answer["add_data_success"])+"下次向我发送“{}”的时候，我就有可能回复“{}”啦~".format(msg.split("+")[0], msg.split("+")[1])
    return choice(except_answer[try_add_data])


def admin_del_data(msg, talk_data):
    try_del_data = del_data(msg, talk_data)
    if try_del_data == False:
        return False
    if try_del_data == True:
        return choice(right_answer["del_data_success"])+"下次向我发送“{}”的时候，我就不再会回复“{}”啦~".format(msg[2:].split("+")[0], msg[2:].split("+")[1])
    return choice(except_answer[try_del_data])


def talk_to_admin(rev, talk_data):
    msg = rev["raw_message"]
    is_code = rcode(msg)
    if is_code[0] == True:
        return is_code[1]
    temp = admin_del_data(msg, talk_data)
    if temp != False:
        return temp
    temp = admin_add_data(msg, talk_data)
    if temp != False:
        return temp
    return None


# --------------------------------------------user----------------------------------------------------
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
}
self_qq = json.load(open("./conf/keys_conf.json"))["self_qq"]

def msg_img_flider(rev):
    msg = rev["raw_message"].replace("[CQ:at,qq={}]".format(self_qq), "").replace(
        " ", "")  # 私聊还@Hex？发空格？爪巴~直接过滤~
    if "[CQ:image,file=" not in msg:
        return [None, msg]  # msg不含有图片
    if msg.count("[CQ:image,file=") > 1:  # 一次识别好几张图片？给爷爬
        return [False, "Hex酱一次只能看一张图片呀~"]
    for i in range(len(rev["message"])):
        if "url" in rev["message"][i]["data"]:
            img_url = rev["message"][i]["data"]["url"]
            break
    try:
        html = requests.get(img_url, headers=header)
        # "http:"开头的图片链接需要get下来然后转base64才能给百度AI识别
        img = base64.b64encode(html.content)
    except:
        # print('获取该图片失败')
        return [False, "Hex酱好像出现了点问题，图片没有下载成功啊~qaq"]
    msg = msg.replace(re.findall("\[CQ:image,file=[A-Za-z0-9.]+]", msg)[0], "")
    # msg只含有一张图片(或还有一些文字) [除图片以外的msg，图片的base64]
    return [True, msg, img, img_url]


def if_send_like(msg, Qnum):
    if msg in ["给我点赞", "点赞", "赞我", "点名片赞", "自动点赞"]:
        if send_like(Qnum):
            return [True, "点赞成功~"]
        else:
            return [True, "好像出现了点错误~"]
    return [False]


def talk_to_user(rev, talk_data):
    msg_img = msg_img_flider(rev)
    # ------------------------------------------------------------------------是否识图
    if msg_img[0] == False:  # 出错就返回报错内容
        return msg_img[1]
    if msg_img[0] == True:
        if_team_cost = team_cost(msg_img[1], msg_img[3], rev["user_id"])
        if if_team_cost[0] == True:  # -------------------------向队内资金管理页面发送记录
            return if_team_cost[1]
        return img_recognizer(msg_img[1], msg_img[2], rev["user_id"])
    msg = msg_img[1]  # 不含有图片的消息就会被过滤到这里
    # ------------------------------------------------------------------------帮助页面
    if_help = help_menu(msg)
    if if_help[0] == True:
        return if_help[1]
    # ------------------------------------------------------------------------发送涩图
    if_setu = hso_pic(msg)
    if if_setu[0] == True:
        return if_setu[1]
    # ------------------------------------------------------------------------是否点赞
    sd_like = if_send_like(msg, rev["user_id"])
    if sd_like[0] == True:
        return sd_like[1]
    # ------------------------------------------------------------------------执行语句
    is_code = rcode(msg)
    if is_code[0] == True:
        return is_code[1]
    # ------------------------------------------------------------------------匹配对话
    return s_talking(msg, talk_data)[1]

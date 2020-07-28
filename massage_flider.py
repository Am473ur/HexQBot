from data.talk_data.deal_talk_data import *
from app.Hex_talker.talk_to import *
from app.Hex_talker.group_talk import *
from random import randint
import json
from httpapi.send_msg import send_msg
main_conf = json.load(open("./conf/main_conf.json"))
self_qq = json.load(open("./conf/keys_conf.json"))["self_qq"]

class msg_talker():
    def __init__(self):
        self.talk_data = load_data()

    def private_msg(self, rev):  # 过滤三种权限(包含关系),developer,admin,user
        if rev["sub_type"] != "friend":
            return send_msg("请先加我为好友呀~", rev["user_id"], "private")
        if rev["user_id"] in main_conf["developer"]:
            will_send = talk_to_developer(rev, main_conf)
            if will_send != None:
                return send_msg(will_send, rev["user_id"], "private")
        #if rev["user_id"] in main_conf["admin"]:
        will_send = talk_to_admin(rev, self.talk_data)
        if will_send != None:
            return send_msg(will_send, rev["user_id"], "private")
        return send_msg(talk_to_user(rev, self.talk_data), rev["user_id"], "private")

    def group_msg(self, rev):
        if "[CQ:at,qq={}]".format(self_qq) in rev["raw_message"]:#"[CQ:at,qq={}]".format(rev["user_id"])+
            return send_msg(answer_at(rev, self.talk_data), rev["group_id"], "group")
        if "[CQ:image,file=" not in rev["raw_message"] and randint(1,10)< 4:
            return send_msg(answer_rd(rev, self.talk_data), rev["group_id"], "group")
        return True

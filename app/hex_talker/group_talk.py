from app.Hex_talker.talk_to import *
from app.HexCTF_Spider.spider import get_ctf_data
from app.CTF_team_info.team_info import ctf_team
from data.talk_data.base_talk import base_talk_data

def answer_at(rev,talk_data):
    msg_img=msg_img_flider(rev)
    if msg_img[0] == False:#出错就返回报错内容
        return msg_img[1]
    if msg_img[0] == True:
        return img_recognizer(msg_img[1],msg_img[2],rev["user_id"])
    msg=msg_img[1] #不含有图片的消息就会被过滤到这里
    #------------------------------------------------------------------------是否点赞
    sd_like=if_send_like(msg,rev["user_id"])
    if sd_like[0] == True:
        return sd_like[1]
    #------------------------------------------------------------------------爬0xCTF
    if msg == "0xCTF":
        return get_ctf_data()
    #------------------------------------------------------------------------队伍分配
    ctfteam=ctf_team(msg,rev["group_id"])
    if ctfteam[0]==True:
        return ctfteam[1]
    #------------------
    return talk_to_user(rev,talk_data)

def answer_rd(rev,talk_data):#这边只回复纯文本的
    if "[CQ:image,file=" in rev["raw_message"]:#如果含有图片，不回答
        return None
    msg=rev["raw_message"].replace(" ", "")
    temp=s_match(msg,talk_data)
    if temp[0]==False:#没有匹配到合适的话，不回答
        return None
    return temp[1]


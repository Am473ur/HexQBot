from random import choice
from data.talk_data.base_talk import others_answer
from app.Hex_talker.fun_words import tianapi

def calculat_score(msg, cmsg):  # msg和候选词
    if msg == "" or cmsg == "":
        return 0
    if msg == cmsg:
        return 1
    a = 1-(abs(len(msg)-len(cmsg))/max(len(msg), len(cmsg)))  # 长度差距评分
    b1 = 0
    for i in msg:
        b1 += (1 if i in cmsg else 0)
    b2 = 0
    for i in cmsg:
        b2 += (1 if i in msg else 0)
    b = ((b1+b2)/2)/min(len(msg), len(cmsg))  # 完全包含是1，不完全包含是相似度 0-1
    return (a*0.2 + b*0.7)  # 满分是1


def s_match(msg, talk_data):
    max_msg = ""
    for row in talk_data:
        temp_score = calculat_score(msg, row[0])
        if temp_score > max_score:
            max_msg, max_score = choice(row[1]), temp_score
    if max_score > 0.8:
        return [True, max_msg]
    # choice(others_answer["no_answer"])
    return [False, choice(others_answer["no_answer"])]

def s_talking(msg, talk_data):
    if_tian=tianapi(msg)
    if if_tian[0]==True:
        return [True,if_tian[1]]
    return s_match(msg, talk_data)
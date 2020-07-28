from app.HexCTF_Spider.spider import get_ctf_data
from httpapi.receive import rev_msg
from massage_flider import msg_talker


talker = msg_talker()
print("start")

while True:
    try:
        rev = rev_msg()
        if rev == None:
            continue
    except:
        continue
    if rev["post_type"] == "message":
        # print(rev)
        if rev["message_type"] == "private":
            talker.private_msg(rev)
        elif rev["message_type"] == "group":
            talker.group_msg(rev)
        elif rev["message_type"] == "discuss":
            continue
        else:
            continue
    elif rev["post_type"] == "notice":
        if rev["notice_type"] == "group_upload":  # 有人上传群文件
            continue
        elif rev["notice_type"] == "group_decrease":  # 群成员减少
            continue
        elif rev["notice_type"] == "group_increase":  # 群成员增加
            continue
        else:
            continue
    elif rev["post_type"] == "request":
        if rev["request_type"] == "friend":  # 添加好友请求
            pass
        if rev["request_type"] == "group":  # 加群请求
            pass
    else:  # rev["post_type"]=="meta_event":
        continue

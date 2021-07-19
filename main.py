from HttpAPI import *
from BaiduImg import *
from common_reply import *
while True:
    recv_json = receive_message()
    if recv_json == None: continue
    print(recv_json)
    if recv_json["post_type"] == "message":
        if recv_json["sub_type"] != "friend":
            send_msg("请先加我为好友呀~", recv_json["user_id"], "private")
        else:
            send_msg(reply(recv_json), recv_json["user_id"], "private")



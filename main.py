from http_api import *

while True:
    recv_json = receive_message()
    if recv_json == None: continue
    if recv_json["post_type"] == "message":
        pass



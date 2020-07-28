import os
from random import choice


def hso_pic(msg):
    if msg in ["来张涩图", "来张色图", "涩图", "色图", "setu", "se图", "ghs"]:
        setu_list = os.listdir("cqp/data/image/setu")
        if len(setu_list) == 0:
            return [True, "啊这，竟然没有库存了"]
        local_img_url = "[CQ:image,file=setu/"+choice(setu_list)+"]"
        return [True, local_img_url]
    if msg in ["色图库存", "涩图库存", "库存涩图", "色图数量", "涩图数量", "有多少张涩图"]:
        setu_list = os.listdir("cqp/data/image/setu")
        return [True, "现在一共有{}张涩图~".format(len(setu_list))]
    return [False]

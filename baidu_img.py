from HttpAPI import *
import requests 
import json
import time

wrong_msg = "「百度智能云API」出现问题啦~"


def update_access_token():
    config_json = json.load(open("config.json"))
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(config_json["BauduImg"]["api_key"],config_json["BauduImg"]["secret_key"])
    response = requests.get(host)
    if response:
        access_token = response.json()["access_token"]
        config_json["BauduImg"]["access_token"] = access_token
        config_json["BauduImg"]["update_time"] = round(time.time())
        json.dump(config_json, open("config.json", "w"), indent=4)
        return [True, access_token]
    return [False]

def img_advanced_general(img, access_token):
    """ 通用物体和场景识别 免费500次/天
    :img: (str) base64 encode
    """
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
    params = {"image": img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        return response.json()
    else:
        return wrong_msg

def img_animal(img, access_token):  # 动物识别 500次/天
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
    params = {"image": img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        temp_json = response.json()
        if "error_code" in temp_json:
            return "好像出了一点问题："+temp_json["error_msg"]
        print(temp_json)
        if response.json()["result"][0]["name"] == "非动物":
            return "我也不认识这是什么动物~换张图片试试吧~"
        return "我在图片上看到的是"+temp_json["result"][0]["name"]  # 返回最有可能的结果
    else:
        return wrong_msg

def img_plant(img, access_token):  # 植物识别 500次/天
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
    params = {"image": img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        if response.json()["result"][0]["name"] == "非植物":
            return "我也不认识这是什么植物~换一张试试吧~"
        return "我在图片上看到的是"+response.json()["result"][0]["name"]  # 返回最有可能的结果
    else:
        return wrong_msg

def img_dish(img, access_token):  # 菜品识别 500次/天
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"
    params = {"image": img, "top_num": 5}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        if response.json()["result_num"]:  # 返回最有可能的结果
            if response.json()["result"][0]["name"] == "非菜":
                return "这是啥菜啊~"
            return response.json()["result"][0]["name"]
    else:
        return wrong_msg

def img_redwine(img, access_token):  # 细粒度图像识别—红酒识别 500次/天---------------------------------------------------------------------
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/redwine"
    params = {"image": img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        # if response.json()["hasdetail"]==1:#有详细信息可以展示~~留坑待填
        #    return None
        print(response.json())
        
        if response.json()["result"]["wineNameCn"] == "":
            return "啊这，Hex酱也看不出这是什么酒啊~"
        return response.json()["result"]["wineNameCn"]  # 没有详细信息
    return wrong_msg

def img_currency(img, access_token):  # 货币识别 100次/天------------------------------------------------------------------------------
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/currency"
    params = {"image": img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        print(response.json())
        if response.json()["result"]["currencyName"] == "":
            return "啊这，Hex酱没有识别出这是什么~"
        if response.json()["result"]["hasdetail"] == 1:  # 有详细信息可以展示
            return "这应该是{}发行的{}面值的{}".format(response.json()["result"]["year"], response.json()["result"]["currencyDenomination"], response.json()["result"]["currencyName"])
        return response.json()["result"]["currencyName"]  # 没有详细信息
    return wrong_msg


def img_landmark(img, access_token):  # 地标识别 免费3000次
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/landmark"
    params = {"image": img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        if response.json()["result"]["landmark"] != "":
            return response.json()["result"]["landmark"]
    return wrong_msg

def img_car(img, access_token):  # 车型识别 500次/天
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"
    params = {"image": img, "top_num": 5}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        if response.json()["result"][0]["name"] == "非车类":
            return "Hex酱看不清啦~换一张试试吧~"
        if response.json()["result"][0]["year"] == "无年份信息":
            return "Hex酱觉得这辆车是"+response.json()["result"][0]["name"]
        if response.json()["color_result"] == "无车辆颜色信息":
            return "这辆车应该是{}，生产年份为{}~".format(response.json()["result"][0]["name"], response.json()["result"][0]["year"])
        return "这辆车应该是{}的{}，生产年份为{}~".format(response.json()["color_result"], response.json()["result"][0]["name"], response.json()["result"][0]["year"])
    return wrong_msg


def img_logo(img, access_token):  # logo商标识别 500次/天
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/logo"
    params = {"custom_lib": False, "image": img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        print(response.json())
        if response.json()["result_num"]:  # 返回最有可能的结果
            return "我看它比较像{}的logo".format(response.json()["result"][0]["name"])
        else:
            return "哎呀~我也不认识这个logo"
    else:
        return wrong_msg

""" 用于给外部调用的函数: handle_picture(msg, img_b64) """
def handle_picture(msg, img_b64):
    """ 处理 [图片]/[文本+图片] 信息
    Args:
        msg (str): 用于辅助选择使用哪一个API
        img_b64 (base64(str)): 图片文件的base64编码
    """
    config_json = json.load(open("config.json"))
    access_token = config_json["BauduImg"]["access_token"]
    update_time = config_json["BauduImg"]["update_time"]
    
    """ 每20天更新一次access_token """
    if (round(time.time()) - update_time)>20*24*3600:
        res_update_access_token = update_access_token()
        if res_update_access_token[0]:
            access_token = res_update_access_token[1]
            send_msg("更新「百度智能云API」Access Token成功～", config_json["admin_qq"], "private")
        else:
            send_msg("更新「百度智能云API」Access Token 失败～", config_json["admin_qq"], "private")
            return "更新「百度智能云API」Access Token 失败～"
    
    general_answer = img_advanced_general(img_b64, access_token)
    if general_answer["result_num"] == 0:
        return [False, "图片上什么都没看到"]
    for i in range(min(2, general_answer["result_num"])):
        if "动物" in general_answer["result"][i]["root"]:
            return [True, img_animal(img_b64, access_token)]
        if "植物" in general_answer["result"][i]["root"]:
            return [True, img_plant(img_b64, access_token)]
        if "食物" in general_answer["result"][i]["root"]:
            return [True, img_dish(img_b64, access_token)]
        if "红酒" in general_answer["result"][i]["keyword"] or "葡萄酒" in general_answer["result"][i]["keyword"]:
            return [True, img_redwine(img_b64, access_token)]
        if "交通工具" in general_answer["result"][i]["root"]:
            return [True, img_car(img_b64, access_token)]
        if "建筑" in general_answer["result"][i]["root"] or "自然风景" in general_answer["result"][i]["root"]:
            return [True, img_landmark(img_b64, access_token)]
        if "货币" in general_answer["result"][i]["root"]:
            return [True, img_currency(img_b64, access_token)]
        if "图标" in general_answer["result"][i]["keyword"]:
            return [True, img_logo(img_b64, access_token)]
    return [False, "图片上有："+general_answer["result"][0]["keyword"]]


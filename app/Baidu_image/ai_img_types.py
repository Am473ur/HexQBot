import requests
from app.Baidu_image.temp_data.msg_data import *

access_token = "xxx"
wrong_msg="出现问题啦~快快联系开发小哥哥~"

def img_advanced_general(img): # 通用物体和场景识别 500次/天
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
    params = {"image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]#请求错误，比如到限额了就直接返回英文/晚点再来填坑
        if response.json()["result_num"]: # 返回最有可能的结果
            return match_advanced_general(response.json()["result"][0]["score"],response.json()["result"][0]["keyword"])#"我在图片上看到的是"+response.json()["result"][0]["keyword"]
    else:
        return wrong_msg

def img_animal(img): # 动物识别 500次/天
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
    params = {"image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        temp_json=response.json()
        if "error_code" in temp_json:
            return "好像出了一点问题："+temp_json["error_msg"]
        print(temp_json)
        if response.json()["result"][0]["name"]=="非动物":
            return "哼~我没发现图片上有动物呀~换张图片试试吧~"
        return "我在图片上看到的是"+temp_json["result"][0]["name"]# 返回最有可能的结果
    else:
        return wrong_msg

def img_plant(img): # 植物识别 500次/天
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"
    params = {"image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response :
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        if response.json()["result"][0]["name"]=="非植物":
            return "哼~我怎么没找到图片上有植物呀~换一张试试吧~"
        return "我在图片上看到的是"+response.json()["result"][0]["name"]# 返回最有可能的结果
    else:
        return wrong_msg

def img_logo(img): # logo商标识别 500次/天
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/logo"
    params = {"custom_lib":False,"image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response :
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        print(response.json())
        if response.json()["result_num"]: # 返回最有可能的结果
            return "我看它比较像{}的logo".format(response.json()["result"][0]["name"])
        else:
            return "哎呀~我也不认识这个logo"
    else:
        return wrong_msg

def img_ingredient(img): # 细粒度图像识别-果蔬 免费3000次
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/classify/ingredient"
    params = {"image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response :
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        print(response.json())
        if response.json()["result_num"]: # 返回最有可能的结果
            if response.json()["result"][0]["name"]=="非果蔬食材":
                return "哼~我在图片上看不到什么果蔬，是不是在骗我~"
            return response.json()["result"][0]["name"]
    else:
        return wrong_msg

def img_dish(img): # 菜品识别 500次/天
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"
    params = {"image":img,"top_num":5}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response :
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        if response.json()["result_num"]: # 返回最有可能的结果
            if response.json()["result"][0]["name"]=="非菜":
                return "哼~我看不到图片上有菜~"
            return response.json()["result"][0]["name"]
    else:
        return wrong_msg

def img_redwine(img): # 细粒度图像识别—红酒识别 500次/天---------------------------------------------------------------------
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/redwine"
    params = {"image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        #if response.json()["hasdetail"]==1:#有详细信息可以展示~~留坑待填
        #    return None
        if response.json()["result"]["wineNameCn"]=="":
            return "啊这，Hex酱在图片上没有找到红酒啊~"
        return response.json()["result"]["wineNameCn"] #没有详细信息
    return wrong_msg

def img_currency(img): # 货币识别 100次/天------------------------------------------------------------------------------
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/currency"
    params = {"image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        print(response.json())
        if response.json()["result"]["currencyName"]=="":
            return "啊这，Hex酱在图片上没有找到货币啊~"
        if response.json()["result"]["hasdetail"]==1:#有详细信息可以展示
            return "这应该是{}发行的{}面值的{}".format(response.json()["result"]["year"],response.json()["result"]["currencyDenomination"],response.json()["result"]["currencyName"])
        return response.json()["result"]["currencyName"] #没有详细信息
    return wrong_msg

def img_landmark(img): # 地标识别 免费3000次
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/landmark"
    params = {"image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response :
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        if response.json()["result"]["landmark"] != "":
            return response.json()["result"]["landmark"]
    return wrong_msg

def img_car(img): # 车型识别 500次/天
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"
    params = {"image":img,"top_num":5}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response :
        print(response.json())
        if "error_code" in response.json():
            return "好像出了一点问题："+response.json()["error_msg"]
        if response.json()["result"][0]["name"]=="非车类":
            return "Hex酱看不到图片上有车啊~换一张试试吧~"
        if response.json()["result"][0]["year"]=="无年份信息":
            return "Hex酱觉得这辆车是"+response.json()["result"][0]["name"] #response.json()["result"]["year"]
        if response.json()["color_result"]=="无车辆颜色信息":
            return "这辆车应该是{}，生产年份为{}~".format(response.json()["result"][0]["name"],response.json()["result"][0]["year"])
        return "这辆车应该是{}的{}，生产年份为{}~".format(response.json()["color_result"],response.json()["result"][0]["name"],response.json()["result"][0]["year"])
    return wrong_msg
'''
def img_object_detect(img): # 图像主体检测-返回坐标 500次/天
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect"
    params = {"image":img,"with_face":1} # face主体是否是人脸
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
'''

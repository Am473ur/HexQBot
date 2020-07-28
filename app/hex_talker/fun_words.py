import json
import requests
tianapi_key = json.load(open("./conf/keys_conf.json"))["tianapi"][0]


def get_word(api_name):
    api_url = "http://api.tianapi.com/txapi/"+api_name+"/index"
    api_url += "?key="+tianapi_key
    res = requests.get(api_url)
    res_code = res.json()["code"]
    if res_code == 200:
        res_word = res.json()["newslist"][0]["content"]
        print(res_code, res_word)
        return res_word
    if res_code == 150:
        return "爬，免费额度嫖完了"


def tianapi(msg):
    if msg in ["舔狗日记", "舔狗"]:
        return [True, get_word("tiangou")]
    if msg in ["彩虹屁"]:
        return [True, get_word("caihongpi")]
    if msg in ["网易云", "网抑云", "到点了"]:
        return [True, get_word("hotreview")]
    if msg in ["土味情话"]:
        return [True, get_word("saylove")]
    return [False]

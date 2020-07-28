import requests 
import json

baiducloud=json.load(open("./conf/keys_conf.json"))["baiducloud"]
# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(baiducloud["client_id"],baiducloud["client_secret"])

response = requests.get(host)
if response:
    print(response.json()['refresh_token'])
#把这里的token复制到keys_conf.json里面既可
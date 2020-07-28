from app.HexCTF_Spider.get_submissions import start_spider

dirr="app/HexCTF_Spider/"

def ctf_data():
    user_data={}
    for count, line in enumerate(open(dirr+"today_data.txt",'r')):#,encoding='UTF-8'
        temp=line.strip().split(",")
        user_data[temp[0]]=temp[1]
    user_data_order=sorted(user_data.items(),key=lambda x:x[1],reverse=True)
    if len(user_data_order)==0:
        return "啊这，最近24小时好像没有提交~"
    show_data="最近24小时内的正确提交：\n"
    for i,j in enumerate(user_data_order):
        show_data+="- {}  {}次\n".format(j[0],j[1])
    show_data+="好棒呀~继续加油~~"
    print(show_data)
    return show_data
 
def get_ctf_data():
    start_spider()
    return ctf_data()

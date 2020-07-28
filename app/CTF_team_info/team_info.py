import json
from random import shuffle
import os
import time


def get_time():
    local_time = [i for i in time.localtime()][:4]
    return local_time


def get_all_contests():
    contests = []
    # send_str="这些是全部记录过的CTF：\n"
    for count, line in enumerate(open("./app/CTF_team_info/CTF_contests.txt", 'r', encoding='UTF-8')):
        temp = line.strip().split("|")
        if len(temp) != 2:
            continue
        temp = [[int(temp[0][:10][:4]), int(temp[0][:10][4:6]), int(temp[0][:10][6:8]), int(temp[0][:10][8:])],
                [int(temp[0][10:][:4]), int(temp[0][10:][4:6]),
                 int(temp[0][10:][6:8]), int(temp[0][10:][8:])],
                temp[1]]
        # send_str+="{}年{}月{}日{}时~{}年{}月{}日{}时——{}\n".format(temp[0][0],temp[0][1],temp[0][2],temp[0][3],temp[1][0],temp[1][1],temp[1][2],temp[1][3],temp[2])
        contests.append(temp)
    return contests


def date_comp(date1, date2):  # date1在date2之前，返回True
    if date1[0] < date2[0]:
        return True
    if date1[0] > date2[0]:
        return False
    if date1[1] < date2[1]:
        return True
    if date1[1] > date2[1]:
        return False
    if date1[2] < date2[2]:
        return True
    if date1[2] > date2[2]:
        return False
    if date1[3] < date2[3]:
        return True
    if date1[3] > date2[3]:
        return False
    return True


def get_past_contests():
    contests = get_all_contests()
    l_time = get_time()
    send_str = "往期比赛：\n"
    for cont in contests:
        if date_comp(cont[1], l_time):
            send_str += "{}——{}年{}月{}日{}点~".format(
                cont[2], cont[0][0], cont[0][1], cont[0][2], cont[0][3])
            if cont[0][0] != cont[1][0]:
                send_str += "{}年{}月{}日{}点\n".format(
                    cont[1][0], cont[1][1], cont[1][2], cont[1][3])
            elif cont[0][1] != cont[1][1]:
                send_str += "{}月{}日{}点\n".format(cont[1]
                                                 [1], cont[1][2], cont[1][3])
            elif cont[0][2] != cont[1][2]:
                send_str += "{}日{}点\n".format(cont[1][2], cont[1][3])
            elif cont[0][3] != cont[1][3]:
                send_str += "{}点\n".format(cont[1][3])
    if send_str == "往期比赛：\n":
        return "目前还没有往期比赛的记录呢"
    return send_str


def get_current_contests():
    contests = get_all_contests()
    l_time = get_time()
    send_str = "当前比赛：\n"
    for cont in contests:
        if date_comp(l_time, cont[1]):
            send_str += "{}——{}年{}月{}日{}点~".format(
                cont[2], cont[0][0], cont[0][1], cont[0][2], cont[0][3])
            if cont[0][0] != cont[1][0]:
                send_str += "{}年{}月{}日{}点\n".format(
                    cont[1][0], cont[1][1], cont[1][2], cont[1][3])
            elif cont[0][1] != cont[1][1]:
                send_str += "{}月{}日{}点\n".format(cont[1]
                                                 [1], cont[1][2], cont[1][3])
            elif cont[0][2] != cont[1][2]:
                send_str += "{}日{}点\n".format(cont[1][2], cont[1][3])
            elif cont[0][3] != cont[1][3]:
                send_str += "{}点\n".format(cont[1][3])
    return send_str[:-1]


def add_contest(contest_name):
    if len(contest_name) <= 20:
        return "添加比赛需要名称和时间呀"
    for i in range(1, 21):
        if contest_name[-i] not in "0123456789":
            return "比赛名称后面的是纯数字日期~"
    if "|" in contest_name:
        return "比赛名称不能包含|符号~"
    c_time = contest_name[-20:]
    c_name = contest_name[:-20]
    text = open("./app/CTF_team_info/CTF_contests.txt", 'r',
                encoding='UTF-8').read()+c_time+"|"+c_name+"\n"
    print(text)
    open("./app/CTF_team_info/CTF_contests.txt",
         'w', encoding='UTF-8').write(text)
    return "添加比赛成功~"


def exit_team(msg, group_id):
    return "爪巴，这个功能还没写完"
    pass

def save_file(filename,data):
    f=open(filename,"w",encoding='UTF-8')
    for i in range(len(data)):
        f.writelines(("".join(["|"+str(j) for j in data[i]]))[1:]+"\n")
    f.close()

def join_team(msg, group_id):
    msg = msg.split("参加")
    if len(msg) != 2 or len(msg[0]) == 0 or len(msg[0]) == 0:
        return "请按照“xxx参加xxCTF”的格式~"
    member, ctf_name= msg[0], msg[1]
    for iname in ["我","人","|","[","]","。",".","?","\\",",",";","，","{","}","~","!","@","$","%","&","#"]:
        if iname in member:
            return "这边建议您换个ID呢"
    contests = get_all_contests()#获取所有的比赛列表
    in_contests=False
    for i in range(len(contests)):#判断该选手要加入的比赛在不在列表
        if ctf_name == contests[i][2]:
            in_contests = True
            break
    if not in_contests:
        return "目前这场比赛的信息还没有添加~"
    c_dir = './app/CTF_team_info/teams'
    ids = os.listdir(c_dir)
    members = ""
    filename = c_dir+"/"+group_id+".txt"
    if group_id + ".txt" in ids:
        data=[]
        for count, line in enumerate(open(filename, 'r', encoding='UTF-8')):
            temp = line.strip().split("|")# CTF名称|分成组数|成员1|成员2|成员3
            data.append(temp)
        for i in range(len(data)):
            if data[i][0] == ctf_name:
                if member not in data[i]:
                    data[i].append(member)
                    save_file(filename,data)
                    return "{}加入成功~".format(member)
                else:
                    return "你已经加入过啦，不要重复加入啊".format(data[0])
        data.append([ctf_name,1,member])
        save_file(filename,data)
        return "{}加入成功~".format(member)
    else:
        open(filename,"w",encoding='UTF-8').write(ctf_name+"|1|"+member)
        return "{}加入成功~".format(member)

def show_ctf_data(ctf_data,n):
    n=int(n) # 分成 n 组, 每组 num 个人
    members=ctf_data[2:]
    send_str=ctf_data[0]+":\n"
    num = len(members)//n
    tar_groups=[]
    for i in range(n):
        tar_groups.append(members[:num])
        members=members[num:]
    for i in range(len(members)):
        tar_groups[i].append(members[i])
    for i in range(len(tar_groups)):
        send_str+="["+("".join([j+"," for j in tar_groups[i]]))[:-1]+"]\n"
    return send_str[:-1]

def random_group(msg, group_id):
    msg = msg.split("随机分成")
    if len(msg) != 2 or len(msg[0]) == 0 or len(msg[0]) <= 1:
        return "请按照“xxxCTF随机分成x组”的格式~"
    if len(msg[1][:-1]) > 1 or msg[1][:-1] not in "123456789":
        return "分成的组数需要是1~9的数字"
    ctf_name, num = msg[0], int(msg[1][:-1])
    c_dir = './app/CTF_team_info/teams'
    ids = os.listdir(c_dir)
    if group_id + ".txt" not in ids:
        return "当前QQ群还没有创建组队信息"
    filename = c_dir+"/"+group_id+".txt"
    data=[]
    for count, line in enumerate(open(filename, 'r', encoding='UTF-8')):
        temp = line.strip().split("|")# CTF名称|分成组数|成员1|成员2|成员3
        data.append(temp)
    for i in range(len(data)):
        if data[i][0] == ctf_name:
            t=data[i][2:]
            shuffle(t)
            data[i]=data[i][:2]+t
            data[i][1]=num
            save_file(filename, data)
            return "随机分组完成~\n"+show_ctf_data(data[i], num)
    return "啊这，没有找到当前QQ群关于{}的成员信息".format(ctf_name)

def get_group_info(msg, group_id):
    c_dir = './app/CTF_team_info/teams'
    ids = os.listdir(c_dir)
    if group_id + ".txt" not in ids:
        return "当前QQ群还没有创建组队信息"
    filename = c_dir+"/"+group_id+".txt"
    data=[]
    for count, line in enumerate(open(filename, 'r', encoding='UTF-8')):
        temp = line.strip().split("|")# CTF名称|分成组数|成员1|成员2|成员3
        data.append(temp)
    for i in range(len(data)):
        if data[i][0] == msg:
            return show_ctf_data(data[i],data[i][1])
    return "啊这，没有找到当前QQ群关于{}的成员信息".format(msg)


# 往期比赛, 当前比赛
# 新增比赛xxxCTF20200723162020072316, 删除比赛xxxCTF20200723162020072316
# ID参加xxxCTF, ID不参加xxxCTF
# xxxCTF随机分成x组
# xxxCTF

def ctf_team(msg, group_id):
    group_id=str(group_id)
    contests = get_all_contests()
    for i in range(len(contests)):
        if msg == contests[i][2]:
            return [True, get_group_info(msg,group_id)]
    if msg[:4] in ["新增比赛","添加比赛","增加比赛"]:
        return [True, add_contest(msg[4:])]
    if msg in ["往期比赛","之前比赛","前期比赛"]:
        return [True, get_past_contests()]
    if msg in ["近期比赛","最近比赛","当前比赛"]:
        return [True, get_current_contests()]
    if msg.count("不参加") == 1:
        return [True, exit_team(msg, group_id)]
    if msg.count("参加") == 1:
        return [True, join_team(msg, group_id)]
    if msg.count("随机分成") == 1:
        return [True, random_group(msg, group_id)]
    return [False]

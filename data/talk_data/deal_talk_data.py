from data.talk_data.base_talk import base_talk_data
import os

num_of_base_talk_data = len(base_talk_data)


def read_file(file_name):
    data = []
    for count, line in enumerate(open("./data/talk_data/"+file_name, 'r', encoding='UTF-8')):
        temp = line.strip().split("|")
        temp = [temp[0], temp[1].split("/")[:-1]]
        data.append(temp)
    return data


def load_data():
    all_file_list = os.listdir("./data/talk_data")
    file_list = []
    all_data = base_talk_data
    for file in all_file_list:
        if file.startswith("trans_talk") and os.path.isfile("./data/talk_data/"+file):
            all_data += read_file(file)
    return all_data


def save_data(all_data):
    all_data = all_data[num_of_base_talk_data:]
    f = open("./data/talk_data/trans_talk_0.txt", 'w', encoding='UTF-8')
    for row in all_data:
        temp = row[0]+"|"+"".join([i+"/" for i in row[1]])
        f.writelines(temp+"\n")
    f.close()


def add_data(add_msg, all_data):  # 不管是什么样的msg都会被送过来测试一下是否想增加关键词
    if add_msg.count(" ") == 1:  # 如果把空格换成加号就完全符合格式的情况，就可能是理解错误，返回一个hint
        if add_msg.split(" ")[0] != "" and add_msg.split(" ")[1] != "":
            return "add_data_hint_0"
    if add_msg.count("+") != 1:  # 如果换成空格不符合格式，加号数量不是1，肯定不是想增加关键词的~
        return False
    if add_msg.split("+")[0] == "" or add_msg.split("+")[1] == "":
        return "add_data_hint_1"
    if "/" in add_msg or "|" in add_msg:
        return "add_data_hint_2"
    msg = add_msg.split("+")
    if len(msg[0]) < 3:
        return "add_data_hint_3"
    for row in all_data:
        if msg[0] == row[0]:
            if msg[1] in row[1]:
                return "add_data_hint_4"
            row[1].append(msg[1])
            save_data(all_data)
            return True
    all_data.append([msg[0], [msg[1]]])
    save_data(all_data)
    return True


def del_data(del_msg, all_data):
    if del_msg[:2] != "rm":
        return False
    if del_msg.count("+") != 1:  # 会使用删除功能的话，就应该已经添加过记录了，就严格一点
        return "del_data_hint_0"
    msg = del_msg[2:].split("+")
    if msg[0] == "" or msg[1] == "":
        return "del_data_hint_1"
    for i in range(len(all_data)):
        if msg[0] == all_data[i][0]:
            if msg[1] in all_data[i][1]:
                if len(all_data[i][1]) == 1:
                    all_data.pop(i)
                    save_data(all_data)
                    return True
                all_data[i][1].remove(msg[1])
                save_data(all_data)
                return True
    return "del_data_hint_2"

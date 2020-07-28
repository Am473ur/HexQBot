import random
import base64
import hashlib

wrong_msg = ["我可运行不了这种呀","不支持这么写啦", "看不懂这种呀", "哎呀，没有运行成功~"]


def keyword_flider(keyword, msg):
    for i in keyword:
        if i not in msg:
            return False
    return True


def py_flider(msg):
    for keyword in ["class", "import", "eval", "exec", "sys", "globals", "_", "builtins", "pow"]:
        if keyword_flider(keyword, msg):
            return False
    return True


def do_python(msg):
    try:
        msg = msg[6:-1]
        if py_flider(msg):
            temp = eval(msg)
        else:
            return random.choice(wrong_msg)
        if temp != None:
            return str(temp)
        else:
            return random.choice(wrong_msg)
    except:
        return random.choice(wrong_msg)


def rcode(msg):
    if msg[:6] == "print(" and msg[-1] == ")":
        return [True, do_python(msg)]
    if (msg[:4] == "md5(" or msg[:4] == "MD5(") and msg[-1] == ")":
        return [True, hashlib.md5(msg[4:-1].encode()).hexdigest()]
    if (msg[:7] == "sha256(" or msg[:7] == "SHA256(") and msg[-1] == ")":
        return [True, hashlib.sha256(msg[7:-1].encode()).hexdigest()]
    if (msg[:7] == "sha512(" or msg[:7] == "SHA512(") and msg[-1] == ")":
        return [True, hashlib.sha512(msg[7:-1].encode()).hexdigest()]
    if msg[:10] == "b64encode(" and msg[-1] == ")":
        return [True, base64.b64encode(msg[10:-1].encode()).decode()]
    if msg[:10] == "b64decode(" and msg[-1] == ")":
        return [True, base64.b64decode(msg[10:-1]).decode()]
    return [None]

from base64 import b64decode
from re import search
import binascii
import sys
from utils import *

enc_msg = "NjM3YTQyNzQ1YTQ0NGUzMg=="
string = ensure_str(enc_msg)
last_tip = "" # 最后的一句提示，在最后解不出来了，就提示一下到哪里解不出来的
convert_path = []
while True:
    flag = False
    # ========== integer ==========
    if search(r'^([0-9])$', string):  # integer
        res = int_to_ascii(string)
        if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))
        else:      last_tip = res[1]

    # ========== binary ==========
    if search(r'^[01]+$', string):  # binary
        res = bin_to_ascii(string)
        if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))
    
    # ==========   hex  ==========
    if search(r'^[a-f0-9]+$', string):
        res = hex_to_ascii(string)
        if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))
        else:      last_tip = res[1]

    # ==========  hash  ==========
    if search(r'^([a-f0-9]{32})$', string) or search(r'^([a-f0-9]{40})$', string) or search(r'^([a-f0-9]{64})$', string) or search(r'^([a-f0-9]{96})$', string) or search(r'^([a-f0-9]{128})$', string)\
    or search(r'^([A-F0-9]{32})$', string) or search(r'^([A-F0-9]{40})$', string) or search(r'^([A-F0-9]{64})$', string) or search(r'^([A-F0-9]{96})$', string) or search(r'^([A-F0-9]{128})$', string):
        res = hashdb(string.lower())
        if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))
        else:      last_tip = res[1]
    
    # ========== Base32 ==========
    if search(r'^[ABCDEFGHIJKLMNOPQRSTUVWXYZ234567]+$', string):
        res = base32_decode(string)
        if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))
        else:      last_tip = res[1]
        
    # ========== Base58 ==========
    if search(r'^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]+$', string):
        res = base58_decode(string)
        if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))
        else:      last_tip = res[1]
    
    # ========== Base64 ==========
    if search(r'^[A-Za-z0-9+\/=]+$', string):
        res = base64_decode(string)
        if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))
        else:      last_tip = res[1]

    # ========== Base85 ==========
    if search(r'^[A-Za-z0-9+\/=]+$', string):
        res = base64_decode(string)
        if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))
        else:      last_tip = res[1]

    # ========== Base91 ==========
    if search(r'^[A-Za-z0-9+\/=]+$', string):
        res = base91_decode(string)
        if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))
        else:      last_tip = res[1]
    if flag == False:
        break

for i in convert_path:
    print(i)
print(last_tip)
print(string)

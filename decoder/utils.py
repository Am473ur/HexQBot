import requests
from base64 import  b32encode, b32decode, b64encode, b64decode, b85encode, b85decode
from base58 import b58decode, b58encode
import base91
import hashlib
import json


def ensure_str(s, encoding='utf-8', errors='strict'):
    """Coerce *s* to `str`.
    For Python 3:
      - `str` -> `str`
      - `bytes or bytearray` -> decoded to `str`
    """
    if not isinstance(s, (str, bytes, bytearray)):
        raise TypeError("not expecting type '%s'" % type(s))
    if isinstance(s, (bytes, bytearray)):
        s = s.decode(encoding, errors)
    return s

def check_ascii(s):
    return all((c < 128 and c > 32) for c in s)

def int_to_ascii(s):
    s_bytes = bytes.fromhex(('0' if len(hex(int(s))[2:])%2 else '') + hex(int(s))[2:])
    try:
        return [True, s_bytes.decode(), "Integer to String"]
    except:
        return [False, "Integer to String failed"]

def bin_to_ascii(s):
    s_num = int(s, 2)
    s_bytes = bytes.fromhex(('0' if len(hex(s_num)[2:])%2 else '') + hex(s_num)[2:])
    if check_ascii(s_bytes):
        return [True, s_bytes.decode(), "Binary to String"]
    return [True, str(s_num), "Binary to Integer"]

def hashdb(s):
    hashs = {32: "MD5", 40: "SHA1", 64: "SHA256", 96: "SHA384", 128: "SHA512"}
    URL = "http://www.ttmd5.com/do.php?c=Decode&m=getMD5&md5={}".format(s)
    try:
        res = requests.post(URL)
        res = json.loads(res.text)
    except:
        return [False, "{} decode failed".format(hashs[len(s)])]
    if (res['flag'] == 1) and ("***" not in res['plain']):
        hash_type = res['type'] if res['type'] != '' else 'md5'
        return [True, res['plain'], hash_type.upper()+" decode"]
    else:
        return [False, "{} decode failed".format(hashs[len(s)])]

def base16_decode(s):
    s_bytes = bytes.fromhex(('0' if len(s)%2 else '') + s)
    try:
        return [True, s_bytes.decode(), "Hex to String"]
    except:
        return [False, "Hex decode failed"]

def base32_decode(s):
    try:
        return [True, b32decode(s.encode()).decode(), "Base32 decode"]
    except:
        return [False, "Base32 decode failed"]

def base58_decode(s):
    try:
        return [True, b58decode(s.encode()).decode(), "Base58 decode"]
    except:
        return [False, "Base58 decode failed"]

def base64_decode(s):
    try:
        return [True, b64decode(s.encode()).decode(), "Base64 decode"]
    except:
        return [False, "Base64 decode failed"]

def base85_decode(s):
    try:
        return [True, b85decode(s.encode()).decode(), "Base85 decode"]
    except:
        return [False, "Base85 decode failed"]

def base91_decode(s):
    try:
        return [True, bytes(base91.decode(s)).decode(), "Base91 decode"]
    except:
        return [False, "Base91 decode failed"]


def test():
    message = ensure_str("Hi~ i'm Hex...")
    MD5 = hashlib.md5(b"123456").hexdigest()
    md5_res = hashdb(MD5)
    if md5_res[0] and md5_res[1] == "123456": print("\033[32m[+]\033[0mRequest hashdb successfully!")
    else:                                     print("\033[31m[!]\033[0mError: Cannot request hashdb!")
    
    test_b16 = base16_decode(message.encode().hex())
    if test_b16[0] and test_b16[1] == message:  print("\033[32m[+]\033[0mSuccess:", test_b16[-1])
    else:                                       print("\033[31m[!]\033[0mError:", test_b16[-1])
    
    test_b32 = base32_decode(b32encode(message.encode()).decode())
    if test_b32[0] and test_b32[1] == message:  print("\033[32m[+]\033[0mSuccess:", test_b32[-1])
    else:                                       print("\033[31m[!]\033[0mError:", test_b32[-1])
    
    test_b58 = base58_decode(b58encode(message.encode()).decode())
    if test_b58[0] and test_b58[1] == message:  print("\033[32m[+]\033[0mSuccess:", test_b58[-1])
    else:                                       print("\033[31m[!]\033[0mError:", test_b58[-1])
    
    test_b64 = base64_decode(b64encode(message.encode()).decode())
    if test_b64[0] and test_b64[1] == message:  print("\033[32m[+]\033[0mSuccess:", test_b64[-1])
    else:                                       print("\033[31m[!]\033[0mError:", test_b64[-1])
    
    test_b85 = base85_decode(b85encode(message.encode()).decode())
    if test_b85[0] and test_b85[1] == message:  print("\033[32m[+]\033[0mSuccess:", test_b85[-1])
    else:                                       print("\033[31m[!]\033[0mError:", test_b85[-1])
    
    test_b91 = base91_decode(base91.encode(message.encode()))
    if test_b91[0] and test_b91[1] == message:  print("\033[32m[+]\033[0mSuccess:", test_b91[-1])
    else:                                       print("\033[31m[!]\033[0mError:", test_b91[-1])
    

if __name__ == '__main__':
    test()

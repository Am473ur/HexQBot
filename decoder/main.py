from utils import ensure_str, int_to_ascii, bin_to_ascii, base16_decode, hashdb, base32_decode, base58_decode, base64_decode, base85_decode, base91_decode
from re import search


def decoder(string):
    string = ensure_str(enc_msg)
    convert_path = []
    while True:
        flag = False
        # ========== integer ==========
        if search(r'^[0-9]+$', string):  # integer
            res = int_to_ascii(string)
            if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))

        # ========== binary ==========
        if search(r'^[01]+$', string):
            res = bin_to_ascii(string)
            if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))
        
        # ==========  Base16  ==========
        if search(r'^[a-f0-9]+$', string) or search(r'^[A-F0-9]+$', string):
            res = base16_decode(string)
            if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))

        # ==========  hash  ==========
        if search(r'^([a-f0-9]{32})$', string) or search(r'^([a-f0-9]{40})$', string) or search(r'^([a-f0-9]{64})$', string) or search(r'^([a-f0-9]{96})$', string) or search(r'^([a-f0-9]{128})$', string)\
        or search(r'^([A-F0-9]{32})$', string) or search(r'^([A-F0-9]{40})$', string) or search(r'^([A-F0-9]{64})$', string) or search(r'^([A-F0-9]{96})$', string) or search(r'^([A-F0-9]{128})$', string):
            res = hashdb(string.lower())
            if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))
        
        # ========== Base32 ==========
        if search(r'^[ABCDEFGHIJKLMNOPQRSTUVWXYZ234567=]+$', string):
            res = base32_decode(string)
            if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))
            
        # ========== Base58 ==========
        if search(r'^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]+$', string):
            res = base58_decode(string)
            if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))
        
        # ========== Base64 ==========
        if search(r'^[A-Za-z0-9+\/=]+$', string):
            res = base64_decode(string)
            if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))

        # ========== Base85 ==========
        if search(r'^[A-Za-z0-9!#$%&()*+-;<=>?@^_`{|}~]+$', string):
            res = base85_decode(string)
            if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))

        # ========== Base91 ==========
        if search(r'^[A-Za-z0-9!#$%&()*+,.\/:;<=>?@\[\]^_`{|}~"]+$', string):
            res = base91_decode(string)
            if res[0]: flag, string = True, res[1]; convert_path.append("{}: {}".format(res[2], res[1]))

        if flag == False:
            break
    return (string, convert_path)

if __name__ == '__main__':
    enc_msg = 'X08yYyIyfEh1VkZHNFB0Yn56UnpEd3w1NE5dWjMraFkrdFVIUzVbPzs3ZipgWkFkS29eZH1oRTZkN3xUcWxDUkw1LkdhMmQxOTFBXUxhdmIoRClhKjp6aipOXmRbQDZke3RpZCV3PT9BTVlEcHdBZWh3XmQhaXw1ZE98U19QQnIiL3BHIzMiOjhJcUhyT3RiMHcxM2E3L0gwTlRlISpoWUQ6W0dqMj0/QjVFXV1aVWIlb15kOWlhWUI4ZlVYT0FSTE1OSCIyNWQhMUFdTGF2YiJPKWFDe0ZOKk41ajYqaWxIOltHe3RwYDpPcUhC'
    # enc_msg = '1100110011011000110000101100111001000000110100101110011001000000110111001101111011101000010000001101000011001010111001001100101'
    string, convert_path = decoder(enc_msg)
    print(string)

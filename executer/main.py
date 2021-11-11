from fastapi import FastAPI
from time import ctime

app = FastAPI()

block_words = ["class", "import", "eval", "exec", "sys", "globals","os", "_", "builtins","getattr", "pow"]

def logger(msg, tag="[+]"):
    with open("executer.log", "a") as f:
        f.write(f"{ctime()}: {tag} {msg}\n")

def finder(keyword, msg):
    for i in keyword:
        if i not in msg: return False
    return True

def block_word(msg):
    for word in block_words:
        if finder(word, msg): return False
    if "**" in msg:           return False
    return True

def eval_msg(code):
    try:
        if block_word(code): 
            temp = eval(code)   
        else:               return [False, 0]
        if temp != None:    return [True, str(temp)]
        else:               return [False, 1]
    except:                 return [False, 2]

@app.get("/executer")
def executer(code):
    logger(code)
    result = eval_msg(code)
    if result[0]:
        logger(result[1], "[~]")
        return {"result":1, "data":result[1]}
    return  {"result":1000+result[1], "data":"error!!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host="0.0.0.0", port=20000)


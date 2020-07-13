# HexQBot

处理 [酷Q](https://cqp.cc/) 插件 [CQHTTP API](https://github.com/richardchien/coolq-http-api) 的上报事件并进行回复的 QQ 群机器人。

目前正在运行的QQ是 2821876761@Hex酱。

## 功能

* **爬取近 24h 内 0xCTF 上的提交情况。** 在 admin 列表中的用户在群里@机器人，会得到 0xCTF 上的近 24h 成功提交次数和对应用户名。
* **私聊调教对话。** 在 admin 列表中的用户可以私聊机器人，发送 help 可以了解如何增/删对话库中的记录。
* **百度 AI 识图。** 调用了百度 AI 的 API，私聊发送图片或在群里@机器人并附一张图片，会得到通用物体识别的结果；发送图片时可以加上关键词（动物/植物/logo/果蔬/菜品/红酒/货币/地点/车）,会得到更具体的答案。
* **执行 Python 语句。** 私聊或在群里@机器人发送 print()，会执行括号内的语句，并回复执行后的返回值（仅括号内的字符串会被执行，使用 eval() 函数，尽管简单过滤了一些输入应该扔有被日的风险）。
* **基础的哈希和编码。** 私聊或在群里@机器人，支持 md5()，sha256()，sha512()，b64encode()，b64decode()，会得到哈希或编/解码后的结果。
* **点名片赞。** 私聊或在群里@机器人，发送 给我点赞/点赞/赞我/点名片赞/自动点赞 可以得到 10 个名片赞。
* **增/删/查 admin 列表用户。** 在 developer 列表中的用户可以分别通过发送 admin+QQ/admin-QQ/admins 来 增/删/查 admin 列表中的 QQ，查找时会同时显示 QQ 和昵称。
* **More...**

## 关于

~~一开始只是想写个群机器人来每天公布0xCTF上的做题情况，然后没忍住多加了一点功能。~~

百度 AI 识图 API 需要 token，每天前 500 次免费，已经在上传的源码中删除了我的 token。

调教的对话存储在txt文件里，出于隐私考虑，上传的文件仅保留了一部分。

## 反馈

如果使用过程中遇到任何问题、Bug，或有其它意见或建议，欢迎提 issue。












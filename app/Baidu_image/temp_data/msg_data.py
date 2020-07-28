from random import choice


def match_advanced_general(score, keyword):
    if score > 0.9:
        return choice(["图片上的是{}~".format(keyword), "这当然是{}啦~".format(keyword), "这是{}哦~".format(keyword)])
    if score > 0.8:
        return choice(["我觉得这是{}~".format(keyword), "这很有可能是{}呀~".format(keyword), "这是{}哦~".format(keyword)])
    if score > 0.7:
        return choice(["我看到的是{}~".format(keyword), "这可能是{}呀~".format(keyword), "我看着很像{}哦~".format(keyword)])
    if score > 0.6:
        return choice(["我看到的是{}~".format(keyword), "这比较像{}呀~".format(keyword), "看着有点像{}哦~".format(keyword)])
    if score > 0.5:
        return choice(["我感觉这可能是{}~".format(keyword), "这可能是{}呀~".format(keyword), "看着有点像{}哦~".format(keyword)])
    if score > 0.4:
        return choice(["这可能是{}？".format(keyword), "有一点像{}哦~".format(keyword)])
    if score > 0.3:
        return choice(["啊这，Hex酱不太确定啦~可能是{}吧？".format(keyword), "可能有一点像{}哦~".format(keyword)])
    if score > 0.2:
        return choice(["啊，看来人家还是太笨啦~这是{}吗？".format(keyword), "我看这个有一点像{}~呜呜呜，看不清~".format(keyword)])
    if score > 0.1:
        return choice(["啊，这是什么呀~难道是{}？".format(keyword), "可能有一点像{}~换一张清晰的好不好呀~".format(keyword)])
    return choice(["啊，这是什么呀~我猜是{}，猜对了吗？".format(keyword), "可能有一点点像{}~换一张给我看试试吧~".format(keyword)])


# "advanced_general":["这是什么"],
msg_to_img = {
    "animal": ["动物", "鸟", "虫", "鱼", "狗"],
    "plant": ["植物", "花", "草", "树", "蘑菇", "叶"],
    "logo": ["标志", "图标", "logo", "Logo", "LOGO", "牌子", "品牌", "商标"],
    "ingredient": ["水果", "蔬菜", "果蔬"],
    "dish": ["菜", "菜品"],
    "redwine": ["红酒", "葡萄酒"],
    "currency": ["货币", "钞票", "币", "钱"],
    "landmark": ["地方", "哪里", "景点", "地点", "楼", "江"],
    "car": ["车"]
}

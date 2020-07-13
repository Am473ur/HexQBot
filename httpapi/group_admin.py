import requests


def group_kick(group_id,user_id):
    ''' group_id:"int",群组号
        user_id:"int",QQ号
    '''
    data = {
            'group_id':group_id,
            'user_id':user_id,
            'reject_add_request':False
    }
    api_url = 'http://127.0.0.1:5700/set_group_kick'
    r = requests.post(api_url,data=data)

def group_ban(group_id,user_id,ban_time=60):
    ''' group_id:"int",群组号
        user_id:"int",QQ号
        ban_time:"int",禁言时间(s)
    '''
    data = {
            'group_id':group_id,
            'user_id':user_id,
            'duration':ban_time
    }
    api_url = 'http://127.0.0.1:5700/set_group_ban'
    r = requests.post(api_url,data=data)
def group_card(group_id,user_id,card):
    ''' group_id:"int",群组号
        user_id:"int",QQ号
        card:"str",成员备注
    '''
    data = {
            'group_id':group_id,
            'user_id':user_id,
            'card':card
    }
    api_url = 'http://127.0.0.1:5700/set_group_card'
    r = requests.post(api_url,data=data)




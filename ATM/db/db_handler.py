'''

数据处理层
    -专门用户处理数据的

'''
#查看数据
from conf import setting
import json, os
def select(username)->tuple:
    #拼接用户信息存放路径
    user_json = os.path.join(setting.USERS_DATE_PATH, f"{username}.json")
    #判断用户信息表是否在文件中，如果存在返回为Ture:
    if os.path.exists(user_json):
        with open(user_json,'r',encoding='utf-8') as f:
            user_dic = json.load(f)
        #存在返回用户字典信息，不存在返回None
        return user_dic
    else:
        return None

def save(user_dic):
    username = user_dic.get("username")
    user_json = os.path.join(setting.USERS_DATE_PATH, f'{username}.json')
    with open(user_json,'wt',encoding='utf-8') as f:
        json.dump(user_dic,f,ensure_ascii=False)
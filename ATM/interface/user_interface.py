'''

存放用户接口层

'''
#存放日志
#注册接口
from lib.common import passwd_md5
def regiseter_interface(username,password,balance=15000):
    from db import db_handler
    #在数据层查找用户信息，判断返回数据是否为None:
    user_dic = db_handler.select(username)
    if user_dic:
        return False,"该用户已存在"
    else:
    # 若用户不存在，组织用户字典
        user_dic = {
                    'username' : username,
                    "password" : password,
                    "balance"  : balance,
                    "flow"     : [],
                    "shop_car" : {},
                    "locked"   : False
                    }
        #保存数据
        db_handler.save(user_dic)
        return True,"用户注册成功"


#登录接口
def login_interface(username,password):
    from db import db_handler
    #在数据层查找用户信息，判断返回数据是否为None:
    user_dic = db_handler.select(username)
    #如果用户不存在，返回错误信息
    if user_dic:
        password_dic = user_dic.get("password").strip()
        if password == password_dic:
            return True,f"用户：【{username}】登录成功"
        else:
            return False,"密码输入错误"
    else:
        return False,"该用户不存在,请重新输入"


def check_balance_interface(username):
    from db import db_handler
    user_dic = db_handler.select(username)
    return f"【{username}】用户的当前余额为:￥{user_dic['balance']}元"



'''

存放用户视图层

'''



# 1.1注册功能---面条版

# def regiseter():
#     while True:
#         username = input("请输入用户名").strip()
#         password = input("请输入密码").strip()
#         re_password = input("确认密码").strip()
#         #在视图函数中可以进行小的逻辑处理，没必要到数据接口层进行处理，比如像两次密码是否一致等
#         #小的逻辑处理层：
#         #1. 如果两次密码一致
#         if password == re_password:
#数据层
#         #2.查看用户是否存在,若用户存在，则让用户重新输入
#             from conf import setting
#             import json, os
#             #查看文件列表中是否有该用户的注册信息，如果有返回初始注册位置
#             user_json = os.path.join(setting.USERS_DATE_PATH, f"{username}.json")
#             #判断用户信息表是否在文件中，如果存在返回为Ture:
#             if os.path.exists(user_json):
#                 print("用于已存在，请重新注册新用户")
#                 continue
#             else:
#接口层
#             #2.若用户不存在，存放用户信息，并初始化用户信息
#             #2.1 初始化用户的数据字典信息 额度 15000或自定义/账户是否被冻结locked(默认为false未冻结状态)/余额/流水flow/购物车shop_car记录
#                 user_dic = {
#                     'username' : username,
#                     "password" : password,
#                     "balance"  : 15000,
#                     "flow"     : [],
#                     "shop_car" : {},
#                     "locked"   : False
#                 }
#             # 2.2 序列化用户字典信息，并进行存放用户信息，对于用户注册信息是给程序员使用，如果很多用户公用一个文件，不方便程序员进行问题排查，所以对于用户信息，建议进行分表存储，那么对于用户信息建议存放至统一的文件夹下面，如db.user_date文件夹，那么我们则需要对存放路径进行配置
#
#
#
#                 with open(user_json,'wt',encoding='utf-8') as f:
#                     json.dump(user_dic,f)
#
#         else:
#             print("两次密码输入信息不一致，请重新输入")
#             continue

#1.2 1注册功能----分层版
#这一部分是用户需要看到的内容
from interface.user_interface import regiseter_interface,login_interface,check_balance_interface,admin_interface
from interface.blank_interface import withdraw_interface,repay_interface,transfer_interface,check_flow_interface
from lib.common import passwd_md5,login_auth


#用户是否登录：
is_load = None
def regiseter():
    while True:
        username = input("请输入用户名").strip()
        password = input("请输入密码").strip()
        re_password = input("确认密码").strip()
        #调用用户注册接口，并为其传参
        if password == re_password:
            psd_has = passwd_md5(password)
            flag,msg = regiseter_interface(username,psd_has)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("两次密码输入信息不一致，请重新输入")
            continue

# 2.登录功能
#问题1：密码明文传输
#问题2：3-9的功能都需要登录后才能使用
def login():

    while True:
        username = input("请输入用户名").strip()
        password = input("请输入密码").strip()
        pwd_hash = passwd_md5(password)
        global is_load
        flag,msg = login_interface(username, pwd_hash)
        if flag:
            is_load = username
            print(msg)
            break
        else:
            print(msg)

# 3.查看余额
@login_auth
def check_balance():
    res = check_balance_interface(is_load)
    print(res)
# 4.提现功能
@login_auth
def withdraw():
    '''
    提现逻辑：
            账户已冻结：提示：账户已被冻结，不能进行提现操作
            账户未冻结：可以提现
            钱不够：提示金额不够
            钱够：余额-提现金额数
    :return: 1.提现成功，当前余额为
            2.提现失败，当前账户被冻结
            3.提现失败，余额不足
    :param:money:提现金额数
    '''
    while True:
        money = input("请输入提现金额:")
        if not money.isdigit():
            print("请输入正确的金额")
            continue
        money = int(money)
        if money>0:
            flag,msg = withdraw_interface(is_load, money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                break
        else:
            print("提现金额不能为负数")

# 5.还款功能
@login_auth
def repay():
    '''
    :return:
    '''
    while True:
        money = input("请输入还款金额:")
        if not money.isdigit():
            print("请输入正确的金额")
            continue
        money = int(money)
        if money>0:
            flag,msg = repay_interface(is_load, money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                break
        else:
            print("还款金额不能为负数")

# 6.转账功能
@login_auth
def transfer():
    '''
    1.输入转账金额
    2.输入转账目标
    :return:
    '''
    while True:
        money = input("请输入转账金额:")
        person = input("请输入转账的人名:")

        if not money.isdigit():
            print("请输入正确的金额")
            continue
        money = int(money)
        if money>0:
            flag,msg = transfer_interface(person, is_load, money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                break
        else:
            print("转账金额不能为负数")

# 7.查看流水
@login_auth
def check_flow():
    flow_list =  check_flow_interface(is_load)

    if flow_list:
        for flow in flow_list:
            print(flow)
    else:
        print("当前账户不存在交易流水")


# 8.购物功能
@login_auth
def shopping():
    pass
# 9.查看购物车
@login_auth
def check_buy_car():
    pass
# 10.管理员功能
@login_auth
def admin():
    '''
    1.添加账户
    2.修改额度
    3.冻结账户
    :return:
    '''
    fuc_dic = {
        "1": ("添加账户", regiseter),
        "2" :  ("修改额度",),
        "3" :  ("账户冻结/解冻",),
        "4" :  ("退出",)}
    while True:
        print("======管理员中心======")
        for k,v in fuc_dic.items():
            print(k, v[0])
        choice = input("请输入功能编号： ").strip()
        if choice not in fuc_dic:
            print("请输入正确功能编号")
            continue
        elif choice == "1":
            (fuc_dic.get(choice))[1]()
        elif choice == "2":
            choice = int(choice)
            balance = int(input("请输入修改额度的金额： ").strip())
            flag,msg = admin_interface(choice,is_load,balance)
            if flag:
                print(msg)
            else:
                print(msg)
        elif choice == "3":
            choice = int(choice)
            flag,msg = admin_interface(choice,is_load)
            if flag:
                print(msg)
            else:
                print(msg)
        else:
            break


#创建函数字典
fuc_dic = {
    "1" :  ("注册功能",regiseter) ,
    "2" :  ("登录功能",login) ,
    "3" :  ("查看余额",check_balance),
    "4" :  ("提现功能",withdraw),
    "5" :  ("还款功能",repay),
    "6" :  ("转账功能",transfer),
    "7" :  ("查看流水",check_flow),
    "8" :  ("购物功能",shopping),
    "9" :  ("查看购物车",check_buy_car),
    "10" : ("管理员功能",admin),
    "11" : ("退出" , )
}

#视图层主程序
def run():
    while True:
        print("======掌上银行======")
        for k,v in fuc_dic.items():
            print(k,v[0])
        print("=======END=======")
        choice = input("请输入功能编号： ").strip()
        if choice not in fuc_dic:
            print("请输入正确功能编号")
            continue
        elif choice == "11":
            break
        (fuc_dic.get(choice))[1]()

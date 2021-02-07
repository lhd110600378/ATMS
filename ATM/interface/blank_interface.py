'''

银行相关接口

'''
# 提现接口
from db import db_handler


def withdraw_interface(username, money):
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
    user_dic = db_handler.select(username)
    balance = user_dic['balance']
    if user_dic['locked']:
        msg = "账户已被冻结，请在前台办理手续"
        return False, msg
    else:
        if balance >= money:
            balance -= money
            user_dic['balance'] = balance
            msg = f"【{username}】提现成功，提现金额为{money}$，当前账户余额为{balance}$"
            user_dic['flow'].append(msg)
            db_handler.save(user_dic)
            return True, msg
        else:
            msg = "当前账户额度不足"
            return False, msg


# 还款接口
def repay_interface(username, repay_money):
    user_dic = db_handler.select(username)
    balance = user_dic['balance']
    if user_dic['locked']:
        msg = "账户已被冻结，请在前台办理手续"
        return False, msg
    else:
        balance += repay_money
        user_dic['balance'] = balance
        msg = f"【{username}】还款成功，还款金额为{repay_money}$，当前账户余额为{balance}$"
        user_dic['flow'].append(msg)
        db_handler.save(user_dic)

        return True, msg


# 转账接口
def transfer_interface(person, username, transfer_moeney):
    user_dic = db_handler.select(username)
    person_dic = db_handler.select(person)
    if person_dic:
        person_balance = person_dic['balance']
        if person_dic['locked']:
            msg = "您转账的账户已被冻结"
            return False, msg
        else:
            if user_dic['locked']:
                msg = "账户已被冻结，请在前台办理手续"
                return False, msg
            else:
                if user_dic['balance'] >= transfer_moeney:
                    user_dic['balance'] -= transfer_moeney
                    person_dic['balance'] += transfer_moeney
                    msg = f"【{username}】转账成功，转账金额为{transfer_moeney}$，【{username}】余额为{user_dic['balance']}$"
                    to_msg = f"【{person}】接收转账成功，转账金额为{transfer_moeney}$，【{person}】余额为{user_dic['balance']}$"
                    user_dic['flow'].append(msg)
                    person_dic['flow'].append(to_msg)
                    db_handler.save(user_dic)
                    db_handler.save(person_dic)
                    return True, msg
                else:
                    msg = "当前账户余额不足"
                    return False, msg
    else:
        msg = '您输入的账户不存在'
        return False, msg


# 查看流水
def check_flow_interface(username):
    user_dic = db_handler.select(username)
    return user_dic['flow']




def defray_interface(username,money):
    user_dic = db_handler.select(username)

    if user_dic.get("balance")>=money:
        user_dic["balance"] = user_dic.get("balance")-money
        db_handler.save(user_dic)
        return True
    else:
        return False



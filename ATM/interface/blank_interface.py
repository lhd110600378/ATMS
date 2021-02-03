'''

银行相关接口

'''
from db import db_handler
def withdraw_interface(username,money):
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
        return False,msg
    else:
        if balance>=money:
            balance-=money
            user_dic['balance'] = balance
            msg =f"提现成功，提现金额为{money}，当前账户余额为{balance}"
            db_handler.save(user_dic)
            return True,msg
        else:
            msg = "当前账户额度不足"
            return False,msg

def repay_interface(username, repay_money):
    user_dic = db_handler.select(username)
    balance = user_dic['balance']
    if user_dic['locked']:
        msg = "账户已被冻结，请在前台办理手续"
        return False, msg
    else:
        balance+=repay_money
        user_dic['balance'] = balance
        db_handler.save(user_dic)
        msg =f"还款成功，还款金额为{repay_money}，当前账户余额为{balance}"
        return True, msg


def transfer_interface(username, transfer_moeney):
    user_dic = db_handler.select(username)
    balance = user_dic['balance']
    if user_dic['locked']:
        msg = "账户已被冻结，请在前台办理手续"
        return False, msg
    else:
        if balance >= transfer_moeney:
            balance -= transfer_moeney
            user_dic['balance'] = balance
            msg = f"转账成功，转账金额为{transfer_moeney}，当前账户余额为{balance}"
            db_handler.save(user_dic)
            return True, msg
        else:
            msg = "当前账户余额不足"
            return False, msg
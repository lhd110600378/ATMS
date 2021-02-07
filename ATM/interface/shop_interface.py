'''

购物商城接口

'''


from db import db_handler
from interface.blank_interface import defray_interface
#添加购车接口：
def add_shopping_car_interface(username,shopping_cart):
    user_dic = db_handler.select(username)
    shop_car = user_dic['shop_car']
    for shoppname,info in shopping_cart.items():
        shop_car.update(
            {shoppname,info}
        )
    db_handler.save(user_dic)
    return True,'添加购车成功'

#商城支付接口
def commodity_payment_interface(username,shopping_cart):
    user_dic = db_handler.select(username)
    shop_car = user_dic.get('shop_car')
    money = 0
    # balance = user_dic['balance']
    # {商品名称：{单价：数量}}
    for shop_name,info in shop_car.items():
        price,num = info.items()
        if shop_name in shopping_cart:
            num+=shopping_cart[shop_name][price]
            money += num*price
        else:
            for k,v in shopping_cart.items():
                price,num = v.items()
                money += price*num
    #添加银行支付接口
    flag = defray_interface(username,money)
    if flag:
        return True,"支付成功"
    else:
        return False,"余额不足"
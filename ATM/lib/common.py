'''

存放公用的方法

'''

#密码加密
from functools import wraps
def passwd_md5(password:str):
    import hashlib
    pwd_md5_obj = hashlib.md5()
    #密码加密
    pwd_md5_obj.update(password.encode('utf-8'))
    #密码加盐
    suger = "月薪两万不是梦"
    pwd_md5_obj.update(suger.encode('utf-8'))
    #取hash值
    pwd_md5 = pwd_md5_obj.hexdigest()
    return pwd_md5


#针对很多功能都需要登录情况下使用，因此做登录装饰器


def login_auth(func):
    from core import src
    @wraps(func)
    def inner(*args,**kwargs):
        if src.is_load:
            res = func(*args,**kwargs)
            return res
        else:
            print("请先登录")
            return src.login()
    return inner
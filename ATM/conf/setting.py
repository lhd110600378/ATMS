'''

配置信息

'''

import os

#获取项目根目录的路径
BASE_PATH = os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    os.pardir,
    os.pardir,
)
)
#获取user_date文件夹路径
USERS_DATE_PATH = os.path.join(
    BASE_PATH, "db", "user_date"
)





print(USERS_DATE_PATH)
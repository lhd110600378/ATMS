'''

项目启动

'''

import os
import sys
print(sys.path)
#添加环境变量
#获取当前目录
sys.path.append(os.path.dirname(__file__))
from core import src

#开始执行项目文件

if __name__ == '__main__':
    #先执行用户视图层
    #先导入scr目录
    #git_test
    src.run()
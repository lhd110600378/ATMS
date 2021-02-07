import zipfile
import random
import time
import sys
import threading
import os



class MyIterator():
    # 单位字符集合
    dirs = os.path.join("1.zip")
    print(dirs)
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz012345678'
    min_digits = 0
    max_digits = 0

    dirs = os.getcwd()
    file_path = os.path.join("1.zip")

    def __init__(self, min_digits, max_digits):
        # 实例化对象时给出密码位数范围，一般4到10位
        if min_digits < max_digits:
            self.min_digits = min_digits
            self.max_digits = max_digits
        else:
            self.min_digits = max_digits
            self.max_digits = min_digits
        self.file_path = os.path.join("1.zip")

    # 迭代器访问定义
    def __iter__(self):
        return self

    def __next__(self):
        rst = str()
        for item in range(0, random.randrange(self.min_digits, self.max_digits + 1)):
            rst += random.choice(MyIterator.letters)
        return rst


def extract():
    start_time = time.time()
    zfile = zipfile.ZipFile()
    for p in MyIterator(4, 6):
        try:
            zfile.extractall(path=".", pwd=str(p).encode('utf-8'))
            print("the password is {}".format(p))
            now_time = time.time()
            print("spend time is {}".format(now_time - start_time))
            sys.exit(0)
        except Exception as e:
            pass

def do_main():

    t1 = threading.Thread(target=extract)
    t2 = threading.Thread(target=extract)
    t3 = threading.Thread(target=extract)
    t4 = threading.Thread(target=extract)
    t5 = threading.Thread(target=extract)
    t6 = threading.Thread(target=extract)
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()
    t4.start()
    t4.join()
    t5.start()
    t5.join()
    t6.start()
    t6.join()

if __name__ == '__main__':
    do_main()

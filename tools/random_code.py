import random


def random_code():
    s = ''  # 创建字符串变量,存储生成的验证码
    for i in range(4):  # 通过for循环控制验证码位数
        num = random.randint(0, 9)  # 生成随机数字0-9
        s = s + str(num)
    return s


if __name__ == '__main__':
    print(random_code())

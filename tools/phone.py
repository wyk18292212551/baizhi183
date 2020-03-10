import re

def check_phone(tel):
    # tel = input("请输入手机号:")
    ret = re.match(r"^1[35678]\d{9}$", tel)

    if ret:
        return True
    else:
        return False


if __name__ == '__main__':
    check_phone('15001857865')
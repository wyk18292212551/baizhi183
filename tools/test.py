import time

from login.views import RED

if __name__ == '__main__':
    RED.setex("iiiii",10,int(time.time()))
    while 1:
        print(RED.get('iiiii'))
        time.sleep(0.5)
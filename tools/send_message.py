import requests

from wyk_cmfw import settings



class YunPian(object):
    '''云片发送单条短信验证
    api_key：唯一标识
    '''
    def __init__(self,api_key):
        self.api_key =api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    # 短信发送的方法
    def send_message(self, mobile, code):
        # 提供短信发送所需的三个参数
        parmas = {
            # "apikey": '40d6180426417bfc57d0744a362dc108',
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【毛信宇test】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code),  # 短信内容必须是已经审核通过的模板

        }

        req = requests.post(self.single_send_url, data=parmas)
        print(req)

if __name__ == '__main__':
    yun_pian = YunPian(settings.APIKEY)
    yun_pian.send_message("13220420120", "8888")

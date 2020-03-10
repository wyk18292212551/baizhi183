import requests

from CMFW_WYK.settings import APIKEY


class YunPian(object):

    def __init__(self, apikey):
        self.api_key = apikey
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_message(self, phone, code):
        # 发送短信的文本必须与已报备的模板内容一致
        parmas = {
            "apikey": self.api_key,
            "mobile": phone,
            "text": "【毛信宇test】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        req = requests.post(self.single_send_url, data=parmas)
        print(req)


if __name__ == '__main__':
    yun_pian = YunPian(APIKEY)
    yun_pian.send_message("18134281412", "123456")
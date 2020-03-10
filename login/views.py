import time

from django.http import HttpResponse
from django.shortcuts import render
from user.models import User
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from redis import Redis

from CMFW_WYK import settings
from tools.phone import check_phone
from tools.send_message import YunPian
from tools.random_code import random_code
RED = Redis(host='127.0.0.1',port=6379)

def login(request):
    return render(request, 'login/login.html')


@csrf_exempt
def get_code(request):
    """
    根据前台用户的手机号为用户生成随机验证码并完成发送
    :param request: 用户手机号
    :return:    发送成功与否
    """

    mobile = request.POST.get('mobile')
    if check_phone(mobile):
        # 先根据手机号去session比对手机号是否已经发送过短信以及时间戳是否满足再次发送的条件
        if RED.get(str(mobile)+"_1"):
            return HttpResponse("请60秒后发送")
        else:
            RED.setex(str(mobile)+"_1",60,int(time.time()))
            # 根据获取到手机号去发送短信
            yunpian = YunPian(settings.APIKEY)
            code = random_code()
            yunpian.send_message(mobile, code)
            RED.setex(str(mobile) + "_2", 600, code)

            # 向session中存入当前手机号与时间戳
            return HttpResponse("发送成功！10分钟内有效！")
    else:
        return HttpResponse("手机号错误")




@csrf_exempt
def check_user(request):

    """
    校验用户登录信息的方法
    :param request:
    :return:
    """
    mobile= request.POST.get('mobile')
    name= request.POST.get('name')
    code= request.POST.get('code')
    request.session['name']=name
    # 判断用户的验证码是否在有效期内
    print(RED.get(str(mobile) + "_2"))
    if RED.get(str(mobile) + "_2"):
        if int(RED.get(str(mobile) + "_2"))==int(code):
            User.objects.create(phone=mobile,account=name)
            return HttpResponse('验证成功')
        else:
            return HttpResponse('验证码错误！')
    else:
        return HttpResponse ('验证码已过期！请重新发送短信')
    # return HttpResponse('验证成功')



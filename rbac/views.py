from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from CMFW_WYK.settings import PERMISSION_LIST
from rbac.models import UserInfo
from rbac.service.init_permission import init_permission


def login(request):
    """
    访问登录表单
    :param request:
    :return:
    """
    return render(request, "login.html")

@csrf_exempt
def check_user(request):
    """
    用户登录请求的方法
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "login.html", {'msg': "请求方法不正确"})

    name = request.POST.get('username')
    pwd = request.POST.get('userpwd')

    user = UserInfo.objects.filter(name=name, password=pwd).first()

    if not user:
        return render(request, "login.html", {"msg": "用户名或密码不正确"})
    request.session['name']=name
    # 完成权限相关的操作
    init_permission(user, request)

    # 用户需要重定向到首页
    return redirect('/lunbo/home')

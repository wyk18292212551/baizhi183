
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from rbac.models import UserInfo
from rbac.service.init_permission import init_permission


def login(request):
    return render(request, "login.html")
@csrf_exempt
def user_login(request):
    """
    用户登陆请求的处理
    :param request:
    :return:
    """
    name = request.POST.get("username")
    pwd = request.POST.get("userpwd")
    print(name,pwd)
    user = UserInfo.objects.filter(name=name, password=pwd).first()
    print(user)
    if not user:
        return render(request, "login.html", {"msg": "账号或密码错误"})
    request.session["name"]=name
    # 权限相关的处理
    init_permission(user, request)
    return redirect("/lunbo/home/")

import time

from django.core.paginator import Paginator
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from lunbo.models import Image


def home(request):
    images = Image.objects.filter(status=1)
    name=request.session.get("name")
    return render(request, 'index.html', {"images": images,"name":name})

def get_lunbo_data(request):
    """
    返回页面所需的用户的json数据
    :param request:
    :return:
    """
    # 获取请求所带参数
    row_num = request.GET.get("rows")
    page_num = request.GET.get("page")
    user_list = Image.objects.all().order_by("id")
    print(user_list,1111)
    all_page = Paginator(user_list, row_num)
    page_list = Paginator(user_list, row_num).page(page_num)
    data = {
        "page": page_num,
        "total": all_page.num_pages,
        "records": all_page.count,
        "rows": list(page_list)
    }

    def myDefault(u):
        if isinstance(u, Image):
            return {
                "title": u.title,
                "status": u.status,
                "description": u.miaoshu,
                "createDate": u.datetime.strftime('%Y-%m-%d'),
                "url": str(u.lunbo_pic),
            }
    user_json = json.dumps(data, default=myDefault)
    return HttpResponse(user_json)
#模态框添加
@csrf_exempt
def add_lunbo_data(request):
    title = request.POST.get('name')
    miaoshu = request.POST.get("miaoshu")
    times = time.strftime('%Y-%m-%d')
    status = request.POST.get('status')
    pic = request.FILES.get('pic')
    try:
        Image.objects.create(title=title, status=status, lunbo_pic=pic,miaoshu=miaoshu, datetime=times)
        print('添加成功')
    except Exception as e:
        print(e,222)
        print('添加失败')
        pass
    return HttpResponse()
@csrf_exempt
def edit_lunbo_data(request):
    """
    编辑用户的实现：获取所需参数，修改删除
    :param request:
    :return:
    """
    oper = request.POST.get("oper")
    name = request.POST.get("title")
    zhuangtai = request.POST.get("status")
    miaoshu = request.POST.get("description")
    if oper == "add":
        # 代表当前是添加操作
        pass
    elif oper == "edit":
        id = request.POST.get("id")
        image = Image.objects.get(pk=id)
        image.title = name
        image.status = zhuangtai
        image.miaoshu = miaoshu
        image.save()
    elif oper == "del":
        id = request.POST.get("id")
        Image.objects.get(pk=id).delete()
    return HttpResponse()








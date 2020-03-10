import json
from django.core.paginator import Paginator
from django.db.models import Count
import datetime
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from redis import Redis
from user.models import User

red = Redis(host='127.0.0.1',port=6379)

@csrf_exempt
def get_user_data(request):
    """
    返回页面所需的用户的json数据
    :param request:
    :return:
    """
    # 获取请求所带参数
    row_num = request.GET.get("rows")
    page_num = request.GET.get("page")
    user_list = User.objects.all().order_by("id")
    all_page = Paginator(user_list, row_num)
    page_list = Paginator(user_list, row_num).page(page_num)
    data = {
        "page": page_num,
        "total": all_page.num_pages,
        "records": all_page.count,
        "rows": list(page_list)
    }
    def myDefault(u):
        if isinstance(u,User):
            return {
                "id": u.pk,
                "title":u.account,
                "status":u.status,
                "address":u.addr,
                "createDate":u.zhuce_time.strftime('%Y-%m-%d'),
                "url": u.header_pic.url,
            }
    user_json = json.dumps(data, default=myDefault)
    return HttpResponse(user_json)


@csrf_exempt
def edit_user_data(request):
    # 获取所需参数
    oper = request.POST.get("oper")
    status = request.POST.get('status')
    if oper == "edit":
        id = request.POST.get("id")
        user = User.objects.get(pk=id)
        user.stutas = status
        user.save()
    return HttpResponse()


def qushi(request):
    before_n_days = []
    for i in range(1,8)[::-1]:
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i)))
    a1 = User.objects.values('zhuce_time').annotate(Count('zhuce_time')).order_by("zhuce_time")
    print(a1)
    data2=[]
    data3=[]
    for j in a1:
        dict3=j
        print(dict3)
        dict3["name"] = dict3.pop("zhuce_time")
        dict3["value"] = dict3.pop("zhuce_time__count")
        data2.append(dict3.get('name'))
        data3.append(dict3.get('value'))
    print(data2,data3)
    data1 = {
        "name": data2,
        "value": data3,
    }

    return JsonResponse(data1, content_type="application/json",safe=False)

def get_map(request):
    a1=User.objects.values('addr').annotate(Count('addr'))
    data=[]
    for i in a1:
        dict2 = i
        dict2["name"] = dict2.pop("addr")
        dict2["value"] = dict2.pop("addr__count")
        data.append(dict2)
    # print(data)
    return HttpResponse(json.dumps(data), content_type="application/json")



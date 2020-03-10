# Create your views here.
import json
import os
import time

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

from article.models import Article, Pic


def getALLArticle(request):
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    article = Article.objects.all().order_by('id')
    all_page = Paginator(article, row_num)
    page = Paginator(article, row_num).page(page_num).object_list

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    for i in page:
        rows.append(i)

    def myDefault(u):
        if isinstance(u, Article):
            return {'id': u.id,
                    'content': u.content,
                    'title': u.title,
                    'status': u.status,
                    'createDate': u.create_date.strftime('%Y-%m-%d'),
                    'publishDate': u.publish_date.strftime('%Y-%m-%d'),
                    }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)
@csrf_exempt
def upload_img(request):
    """
    富文本编辑器上传图片的实现
    :param request:
    :return:  {"error":0,"url":"\/ke4\/attached\/W020091124524510014093.jpg"}
    """
    image = request.FILES.get("imgFile")
    print(image)

    if image:
        img_url = request.scheme + "://" + request.get_host() + "/static/static/img/" + str(image)
        # print(img_url,1111111111)
        Pic.objects.create(pic=image)
        result = {"error": 0, "url": img_url}
    else:
        result = {"error": 1, "url": "上传失败"}
    return HttpResponse(json.dumps(result), content_type="application/json")
def query_img(request):
    """
    富文本编辑器空间的方法实现
    :param request:
    :return:  准备好的图片格式
    """

    pic_url = request.scheme + "://" + request.get_host() + "/static/"
    pic_list = Pic.objects.all()
    print(pic_list)
    rows = []
    for pic in list(pic_list):
        pic_suffle = os.path.splitext(pic.pic.url)[1]
        rows.append({
            "is_dir": False,
            "has_file": False,
            "filesize": pic.pic.size,
            "dir_path": "",
            "is_photo": True,
            "filetype": pic_suffle,
            "filename": pic.pic.name,
            "datetime": "2018-06-06 00:36:39"
        })

    data = {
        "moveup_dir_path": "",
        "current_dir_path": "",
        "current_url": pic_url,
        "total_count": len(pic_list),
        "file_list": rows,
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
@csrf_exempt
def add_article(request):
    try:
        timess = time.strftime('%Y-%m-%d')
        content = request.GET.get("content")
        title = request.GET.get("title")
        status = request.GET.get("status")
        print(content)
        if content != None:
            Article.objects.create(title=title,status=status,create_date=timess,publish_date=timess,content=content)
            return JsonResponse({"error": "0"})
        else:
            return JsonResponse({"error": 1, "msg": "请认真填写信息！"})
    except:
        return redirect("index:index")
def xiugai(request):
    try:
        ids = request.GET.get("id")
        content = request.GET.get("content2")
        title = request.GET.get("title2")
        status = request.GET.get("status2")
        print(content,title,status,id)
        User2s = Article.objects.get(id=ids)
        if content !=None:
            User2s.title = title
            User2s.content=content
            User2s.status = status
            print(User2s.status)
            User2s.save()
            return JsonResponse({"error":0})
        return JsonResponse({"error": 1, "msg": "请认真填写信息！"})
    except:
        return redirect("index:index")
@csrf_exempt
def edit(request):
    """
    编辑用户的实现
    :param request:
    :return:
    """
    # 获取所需参数
    oper = request.POST.get("oper")
    print(oper)
    if oper == "del":
        id = request.POST.get("id")
        Article.objects.get(pk=id).delete()
    return HttpResponse()


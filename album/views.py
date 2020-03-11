import json
import time
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from mutagen.mp3 import MP3

from album.models import Zhuanji, Zhangjie
def get_album_data(request):
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')
    rows = []
    album = Zhuanji.objects.all().order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)

    for i in page:
        rows.append(i)



    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u,Zhuanji):
            return {
                "author": u.author,
                "brief": u.brief,
                "broadcast": u.boyin,
                "count": u.count,
                "cover": u.album_pic.url,
                "id": u.id,
                "publishDate": u.shangchuan_date.strftime('%Y-%m-%d'),
                "score": u.score,
                "status": u.status,
                "title": u.title,
            }
    data = json.dumps(page_data, default=myDefault)
    return HttpResponse(data)

@csrf_exempt
def get_chapter_data(request):
    albumId = request.GET.get("albumId")
    print(albumId)
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')
    rows = []
    # 根据专辑的id查询出该专辑对应的所有的章节
    album = Zhangjie.objects.all().filter(album_id=albumId)
    print(album)
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)
    for i in page:
        rows.append(i)
    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }
    def myDefault(u):
        if isinstance(u, Zhangjie):
            urls =u.url.url
            print(u.url,type(urls))
            return {
                "createDate": u.create_date.strftime('%Y-%m-%d'),
                "id": u.id,
                "title": u.title,
                "size": u.size,
                "url": urls,
                "duration": u.duration,
            }
    data = json.dumps(page_data, default=myDefault)
    return HttpResponse(data)

@csrf_exempt
def edit_album(request):

    """
    编辑用户的实现
    :param request:
    :return:
    """
    # 获取所需参数
    oper = request.POST.get("oper")
    print(oper)
    name = request.POST.get("title")
    zuozhe = request.POST.get("author")
    zhangjieshu = request.POST.get("count")
    jianjie = request.POST.get("brief")
    zhuangtai = request.POST.get("status")
    gengxinshijian = request.POST.get("publishDate")

    # pwd = request.POST.get("")
    if oper == "edit":
        id = request.POST.get("id")
        user = Zhuanji.objects.get(pk=id)
        user.title = name
        user.author = zuozhe
        user.count = zhangjieshu
        user.brief = jianjie
        user.status=zhuangtai
        user.shangchuan_date = gengxinshijian
        user.save()
    elif oper == "del":
        id = request.POST.get("id")
        Zhuanji.objects.get(pk=id).delete()
    return HttpResponse()

@csrf_exempt
def add_album(request):
    timess = time.strftime('%Y-%m-%d')
    biaoti = request.POST.get("biaoti")
    fenshu = request.POST.get("fenshu")
    zuozhe = request.POST.get("zuozhe")
    boyin = request.POST.get("boyin")
    zhangjieshu = request.POST.get("zhangjieshu")
    jianjie = request.POST.get("jianjie")
    status = request.POST.get("status")
    pic = request.FILES.get("pic")
    faxingshijian = request.POST.get("faxingshijian")
    print(pic)
    if biaoti != None or status != None:
        Zhuanji.objects.create(title=biaoti,score=fenshu,author=zuozhe,boyin=boyin,count=zhangjieshu,brief=jianjie,fabu_date=faxingshijian,album_pic=pic,status=status,shangchuan_date=timess)
        return JsonResponse({"error":"0"})
    else:
        return JsonResponse({"error":1,"msg":"请认真填写信息！"})


@csrf_exempt
def add_chapter(request):
    title = request.POST.get('zhangjieming')
    albumId = request.POST.get('idss')
    file_name = request.FILES.get('mmpp3')
    print(file_name)
    time_long=MP3(file_name)
    time_long=time_long.info.length
    a= int(time_long/60)
    b= int(time_long%60)
    time_long=str(a)+':'+str(b)+str("分")
    size= file_name.size
    size=round(int(size)/1024/1024,2)
    size = str(size)+"mb"
    date_time = time.strftime('%Y-%m-%d')
    if title != None or file_name != None:
        Zhangjie.objects.create(title=title,url=file_name, size=size, album_id=albumId,create_date=date_time,duration=time_long,audio="daiding")
        return JsonResponse({"error": "0"})
    else:
        return JsonResponse({"error": 1, "msg": "请认真填写信息！"})
@csrf_exempt
def edit_chapter(request):
    """
    编辑用户的实现
    :param request:
    :return:
    """
    # 获取所需参数
    oper = request.POST.get("oper")
    print(oper)
    name = request.POST.get("title")
    createDate = request.POST.get("createDate")
    if oper == "edit":
        id = request.POST.get("id")
        user = Zhangjie.objects.get(pk=id)
        user.title = name
        user.create_date = createDate
        user.save()
    elif oper == "del":
        id = request.POST.get("id")
        Zhuanji.objects.get(pk=id).delete()
    return HttpResponse()





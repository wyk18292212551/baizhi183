
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from album.models import Zhuanji, Zhangjie
from article.models import Article
from lunbo.models import Image
from user.models import User


def index_get(request):
    uid = request.GET.get("uid")
    types = request.GET.get("type")
    sub_type = request.GET.get("sub_type")
    data = {
        "header": [],
        "body": [],
        "album": [],
        "article": []
    }
    if types == "all":
        lunbotu = Image.objects.all()
        print(lunbotu)
        for i in lunbotu:
            headers = {
                "thumbnail": request.scheme + "://" + request.get_host() + '/static' + i.lunbo_pic.url,
                "desc": i.miaoshu,
                "id": i.pk,
            }
            data["header"].append(headers)
        zhuanji = Zhuanji.objects.all()
        for zj in zhuanji:
            zjs = {
                "thumbnail": request.scheme + "://" + request.get_host() + zj.album_pic.url,
                "title": zj.title,
                "author": zj.author,
                "type": "0",
                "set_count": zj.count,
                "create_date": zj.shangchuan_date.strftime('%Y.%m.%d')
            }
            data["body"].append(zjs)
        wenzhang = Article.objects.all()
        for wz in wenzhang:
            wzs = {
                "title": wz.title,
                "author": wz.new_img,
                "type": "1",
                "create_date": wz.create_date.strftime('%Y.%m.%d')
            }
            data["body"].append(wzs)
    elif types == "wen":
        zj2 = Zhuanji.objects.all()
        for zhuan in zj2:
            zj22 = {
                "thumbnail": request.scheme + "://" + request.get_host() + zhuan.album_pic.url,
                "title": zhuan.title,
                "author": zhuan.author,
                "set_count": zhuan.count,
                "create_date": zhuan.shangchuan_date.strftime('%Y.%m.%d')
            }
            data["album"].append(zj22)
    elif types == "si":
        ssyjs = Article.objects.all()
        if sub_type == 'ssyj':
            for shang1 in ssyjs:
                ssyj2 = {
                    "title":shang1.title,
                    "author":shang1.status,
                    "create_data":shang1.create_date.strftime('%Y.%m.%d')
                }
                data["article"].append(ssyj2)
        elif sub_type == 'xmfy':
            for shang in ssyjs:
                ssyj2 = {
                    "title":shang.title,
                    "author":shang.status,
                    "create_data":shang.create_date.strftime('%Y.%m.%d')
                }
                data["article"].append(ssyj2)
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def zhuanji_get(request):
    id = request.GET.get("id")
    uid = request.GET.get("uid")
    data = {
        "list":[],
        "introduction":''
    }
    zjzs = Zhuanji.objects.filter(id=id)[0]
    if zjzs:
        data["introduction"] = {
            "thumbnail":request.scheme+"://"+request.get_host()+"/static/"+zjzs.album_pic.url,
            "title":zjzs.title,
            "score":zjzs.score,
            "author":zjzs.author,
            "broadcast":zjzs.boyin,
            "set_count":zjzs.count,
            "brief":zjzs.brief,
            "create_data":zjzs.fabu_date.strftime('%Y.%m.%d')
        }

    zhangjie_get = Zhangjie.objects.filter(album_id=id)
    if zhangjie_get:
        for zj_get in zhangjie_get:
            zj_get2 = {
                "title":zj_get.title,
                "downlooad_url":request.scheme+"://"+request.get_host()+zj_get.url.url,
                "size":zj_get.size,
                "duration":zj_get.duration
            }
            data["list"].append(zj_get2)
    return HttpResponse(json.dumps(data),content_type="application/json")



def user_get(request):
    id = request.GET.get("uid")
    users = User.objects.all()
    get_user = []
    for user_get in users:
        get_user.append({
            "farmington":user_get.faming,
            "nickname":user_get.account,
            "gender":user_get.sex,
            "photo":request.scheme+"://"+request.get_host()+user_get.header_pic.url,
            "location":user_get.code,
            "province":user_get.addr,
            "city":user_get.addr+"暂无字段",
            "description":user_get.qianming,
            "phone":user_get.phone
        })
    return HttpResponse(json.dumps(get_user),content_type="application/json")



@csrf_exempt
def user_post(request):
    uids = request.POST.get("uid")

    gender = request.POST.get("gender")
    location = request.POST.get("location")
    description = request.POST.get("description")
    nickname = request.POST.get("nickname")
    province= request.POST.get("province")
    password = request.POST.get("password")
    city = request.POST.get('city')
    print(uids)
    userss = User.objects.filter(pk=uids)[0]
    # print(userss)
    user_posts = []
    if userss:
        userss.sex = gender
        userss.code = location
        userss.qianming = description
        userss.account = nickname
        userss.addr = province
        userss.password = password
        userss.save()
        data = {
            "password":userss.password,
            "farmington":userss.faming,
            "uid":userss.pk,
            "nickname":userss.account,
            "gender":userss.sex,
            # "photo":request.scheme+"://"+request.get_host()+user_get+userss.header_pic,
            "location":userss.code,
            "province":userss.addr,
            "city":userss.addr+"暂无字段",
            "description":userss.qianming,
            "phone":userss.phone
        }
        user_posts.append(data)
    else:
        data = {
            "error":"-200",
            "error_msg":"该手机号已经存在"
        }
    return HttpResponse(json.dumps(data), content_type='application/json')






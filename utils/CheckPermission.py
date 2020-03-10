import re

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from CMFW_WYK.settings import PERMISSION_LIST

class CheckPermission(MiddlewareMixin):
    """
    中间件检验用户信息的权限
    """
    def process_request(self, request):
        """
        此方法在用户登陆成功后，重定向到主页之前执行
        :param request:
        :return:
        """
        """
        1. 获取用户当前请求的url
        2. 获取当前用户所拥有的权限列表
        3. 权限信息进行匹配
        """
        # 白名单
        valid_url_list = [
            '/rbac/login/',
            '/rbac/user_login/',
            '/admin/.*',
        ]

        current_url = request.path_info
        for url in valid_url_list:
            if re.match(url, current_url):
                # 通过匹配在白名单中的路由都无需拦截
                return None

        # 获取当前用户在session中的权限
        permission_list = request.session.get(PERMISSION_LIST)

        if not permission_list:
            return HttpResponse("请登陆")
        # 比对当前用户访问的url是否在权限列表中
        for url in permission_list:
            if url == current_url:
                return None

        return HttpResponse("无权访问")

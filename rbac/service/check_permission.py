import re

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from CMFW_WYK.settings import PERMISSION_LIST


class CheckPermission(MiddlewareMixin):
    """
    用户权限信息的校验
    """

    def process_request(self, request):
        """
        当用户请求进入到view之前执行
        :param request:
        1. 获取当前用户要访问的url
        2. 获取当前用户的权限列表
        3. 进行权限匹配
        :return:
        """
        # 设置白名单，对于无需拦截的请求进行放行
        valid_url_list = [
            '/rbac/login/',
            '/rbac/check_user/',
            '/admin/.*',
            ' '
        ]
        current_url = request.path_info
        per_list = request.session.get(PERMISSION_LIST)

        for url in valid_url_list:
            if re.match(url, current_url):
                return None

        if not per_list:
            return HttpResponse("请登录")

        # 判断当前用户访问的url与用户所拥有的权限url是否匹配
        for url in per_list:
            # 使用正则判断
            if url == current_url:
                return None

        return HttpResponse('无权访问')

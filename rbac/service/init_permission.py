from CMFW_WYK.settings import PERMISSION_LIST, MENU_LIST


def init_permission(user, request):
    """
    完成权限相关的方法
    :return:
    """
    # 如果当前用户登录请求合法，则查询当前用户所拥有的权限
    permissions = user.roles.filter(permissions__isnull=False).values('permissions__url',
                                                                      'permissions__title',
                                                                      'permissions__is_menu').distinct()

    # 获取权限列表
    permissions_list = [item['permissions__url'] for item in permissions]

    menu_list = []
    # 获取当前用户所拥有的权限中，能够成为菜单的url
    for item in permissions:
        # 判断用户权限的url哪些是菜单，将所有是菜单的url放入列表中
        if item['permissions__is_menu']:
            temp = {
                'title': item['permissions__title'],
                'url': item['permissions__url'],
            }
            menu_list.append(temp)

    # 将菜单的权限列表存入session
    request.session[MENU_LIST] = menu_list

    # 将用户的权限存入session
    request.session[PERMISSION_LIST] = list(permissions_list)

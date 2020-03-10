from CMFW_WYK.settings import PERMISSION_LIST, MENU_LIST


def init_permission(user, request):
    """
    用户权限的初始化
    :param user:
    :param request:
    :return:
    """
    # 用户登陆成功后获取该用户所拥有的所有的权限
    # 获取用户权限中能够成为菜单的url
    roles = user.roles.filter(permissions__isnull=False).values(
        "permissions__url",
        "permissions__is_menu",
        "permissions__title",).distinct()
    print(roles,'获取当前角色权限列表')
    # 获取用户拥有的url
    permission_list = []
    # 能够成为菜单的url
    menu_list = []
    for item in roles:
        permission_list.append(item["permissions__url"])
        if item["permissions__is_menu"]:
            temp = {
                "title": item["permissions__title"],
                "url": item["permissions__url"],
            }
            menu_list.append(temp)
    print(menu_list)
    # 将用户所有的权限存入session
    request.session[PERMISSION_LIST] = permission_list
    # 当前用户所拥有的菜单
    request.session[MENU_LIST] = menu_list

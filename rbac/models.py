from django.db import models

class Permission(models.Model):
    title = models.CharField(verbose_name="权限名称", max_length=40)
    url = models.CharField(verbose_name="权限的url", max_length=128)
    is_menu = models.BooleanField(default=False, verbose_name="是否是菜单")
    # menu = models.ForeignKey(to="Menu", verbose_name="菜单", null=True, blank=True, help_text="null表示不是菜单",on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Role(models.Model):
    title = models.CharField(verbose_name="角色名称", max_length=40)
    permissions = models.ManyToManyField(verbose_name="角色所拥有的权限", to="Permission", blank=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    name = models.CharField(verbose_name="用户名", max_length=40)
    password = models.CharField(verbose_name="密码", max_length=64)
    roles = models.ManyToManyField(to="Role", verbose_name="用户所拥有的角色", blank=True)

    def __str__(self):
        return self.name

# class Menu(models.Model):
#     title = models.CharField(verbose_name="菜单", max_length=80)


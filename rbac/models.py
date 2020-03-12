from django.db import models


# Create your models here.

class Permission(models.Model):
    title = models.CharField(verbose_name="权限名称", max_length=40)
    url = models.CharField(verbose_name="权限url", max_length=200)
    is_menu = models.BooleanField(verbose_name="是否是菜单", default=False)

    def __str__(self):
        return self.title


class Role(models.Model):

    title = models.CharField(verbose_name="角色名称", max_length=40)
    permissions = models.ManyToManyField(to="Permission", verbose_name="角色所对应的权限", blank=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):

    name = models.CharField(verbose_name="用户名", max_length=40)
    password = models.CharField(verbose_name="密码", max_length=64)
    roles = models.ManyToManyField(verbose_name="用户所拥有的角色", to='Role', blank=True)

    def __str__(self):
        return self.name
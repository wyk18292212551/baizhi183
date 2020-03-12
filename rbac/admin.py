from django.contrib import admin

# Register your models here.
from rbac import models

# 必须注册后才可以再django的后台站点中看到表
admin.site.register(models.UserInfo)
admin.site.register(models.Permission)
admin.site.register(models.Role)

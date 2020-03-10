from django.db import models

class User(models.Model):
    phone = models.CharField(max_length=100,null=True)
    account = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    header_pic = models.ImageField(upload_to="header_pics",null=True)
    faming = models.CharField(max_length=100,null=True)
    sex = models.CharField(max_length=100,null=True)
    addr = models.CharField(max_length=100,null=True)
    qianming = models.TextField(null=True)
    status = models.CharField(max_length=100,null=True)
    code = models.CharField(max_length=100,null=True)
    zhuce_time = models.DateField(blank=True,null=True)
    class Meta:
        db_table="user"


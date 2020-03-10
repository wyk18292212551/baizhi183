from django.db import models

class User(models.Model):
    phone = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    header_pic = models.ImageField(upload_to="header_pics")
    faming = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    qianming = models.TextField()
    status = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    zhuce_time = models.DateField(blank=True)
    class Meta:
        db_table="user"


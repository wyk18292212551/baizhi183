from django.db import models


class Zhuanji(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    boyin = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    brief = models.CharField(max_length=255, blank=True, null=True)#jianjie
    fabu_date = models.DateField(blank=True, null=True)
    album_pic = models.ImageField(upload_to="album_pic")
    status = models.CharField(max_length=255, blank=True, null=True)
    shangchuan_date = models.DateField(blank=True, null=True)
    class Meta:
        db_table = 'zhuanji'


class Zhangjie(models.Model):

    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.FileField(upload_to="zhangjie_pics")
    size = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    album_id = models.CharField(max_length=36, blank=True, null=True)
    audio = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        db_table = 'zhangjie'

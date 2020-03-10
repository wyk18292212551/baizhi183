from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    miaoshu = models.TextField()
    datetime = models.DateTimeField(blank=True,null=True)
    lunbo_pic = models.ImageField(upload_to="lunbo_pics")

    class Meta:
        db_table = "image"

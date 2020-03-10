from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    guru_id = models.CharField(max_length=11, blank=True, null=True)
    new_img = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'article'
class Pic(models.Model):
    pic = models.ImageField(upload_to="static/img")
    class Meta:
        db_table = "pic"

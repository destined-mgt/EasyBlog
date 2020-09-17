from django.db import models


class Article(models.Model):
    article_text = models.TextField(max_length=200)
    article_title = models.CharField(max_length=50)
    article_id = models.AutoField(primary_key=True)

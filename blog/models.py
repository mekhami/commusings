from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    teaser = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

class Category(models.Model):
    title=models.CharField(max_length=56)
    articles=models.ManyToManyField(Article)

class Comment(models.Model):
    content = models.TextField()
    user = models.EmailField()
    subject = models.CharField(max_length=128)
    article = models.ForeignKey(Article)

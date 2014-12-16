from django.db import models
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    teaser = models.CharField(max_length=200, default="", null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

class Category(models.Model):
    title=models.CharField(max_length=56)
    articles=models.ManyToManyField(Article)

class Comment(models.Model):
    content = models.TextField()
    user = models.CharField(max_length=56)
    subject = models.CharField(max_length=128)
    article = models.ForeignKey(Article)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user + ' ' + self.subject


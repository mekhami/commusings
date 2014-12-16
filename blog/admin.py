from django.contrib import admin
from .models import Article, Comment

# Register your models here.
admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    exclude = ('slug',)
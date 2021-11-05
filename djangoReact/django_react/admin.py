from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
  list = ('title', 'description',)

admin.site.register(Article, ArticleAdmin)

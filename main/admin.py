from django.contrib import admin
from .models import Article, ArticleSeries

class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'subtitle',
        'slug',
        # 'published',
    ]

class ArticleAdmin(admin.ModelAdmin):
    # fields = [
    #     'title',
    #     'subtitle',
    #     'article_slug',
    #     'content',
    #     #'published',
    #     'modified',
    #     'series',
    # ]

    fieldsets = [
        ("Header", {'fields': ["title", "subtitle", "article_slug", "series"]}),
        ("Content", {"fields": ["content", "notes"]}),
        ("Date", {"fields": ["modified"]})
    ]
# Register your models here.
admin.site.register(ArticleSeries, ArticleSeriesAdmin)
admin.site.register(Article, ArticleAdmin)


# admin.site.register(ArticleSeries)
# admin.site.register(Article)
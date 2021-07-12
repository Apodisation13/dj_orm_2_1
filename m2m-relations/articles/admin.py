from django.contrib import admin

from .models import Article, Tag, TagThrough


class TagThroughInline(admin.TabularInline):
    model = TagThrough
    # formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagThroughInline]
    # list_display = ['title', 'published_at']
    # search_fields = ['title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

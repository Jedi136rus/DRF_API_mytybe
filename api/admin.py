from django.contrib import admin
from .models import Post, Comment, Follow


class PostAdmin(admin.ModelAdmin):
    list_display = ("text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("author", "post")
    search_fields = ("text",)
    list_filter = ("author",)
    empty_value_display = "-пусто-"


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(Follow)

from django.contrib import admin
from comments.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'map', 'content','created_at')

admin.site.register(Comment,CommentAdmin)

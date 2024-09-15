from django.contrib import admin
from .models import Task, Comment, Tag


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'owner', 'deadline_date')
    search_fields = ('title', 'description')
    list_filter = ('deadline_date', 'author')

    inlines = [
        CommentInline,
    ]


admin.site.register(Task, TaskAdmin)
admin.site.register(Tag)

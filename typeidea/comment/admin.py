from django.contrib import admin

from .models import Comment
from typeidea.custom_site import custom_site

# Register your models here.
@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
    fields = (
        ('target', 'nickname'),
        'content',
        'website',
    )

    search_fields = ['target', 'nickname']
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True

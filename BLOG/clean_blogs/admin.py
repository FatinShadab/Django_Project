from django.contrib import admin
from clean_blogs.models import Contact, SocialUrl, BlogPost, FilesUpload, Projects, Video


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Contact)
admin.site.register(Video)
admin.site.register(SocialUrl)
admin.site.register(Projects)
admin.site.register(BlogPost, PostAdmin)
admin.site.register(FilesUpload)

from django.contrib import admin
from .models import Comment,Image,tags,Like,Profile

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

admin.site.register(Comment)
admin.site.register(Image,ImageAdmin)
admin.site.register(tags)
admin.site.register(Like)
admin.site.register(Profile)

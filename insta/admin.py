from django.contrib import admin
from .models import Comment,Image,tags

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

admin.site.register(Comment)
admin.site.register(Image,ImageAdmin)
admin.site.register(tags)
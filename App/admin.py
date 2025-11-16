from django.contrib import admin
from . models import Teacher
from django.utils.html import mark_safe
@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ('name','t_id','email','image')
    search_fields = ('name','t_id')

    def image_tag(self,obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}"')
    image_tag.short_description = 'Image'
# admin.site.register(Teacher)




# Register your models here.

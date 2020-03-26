from django.contrib import admin

# Register your models here.
# Register your models here.
from django.contrib import admin
from found.models import KindF, PageF

class PageFAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

class KindFAdmin(admin.ModelAdmin):
    list_display = ('name','views', 'likes','slug')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(KindF,KindFAdmin)
admin.site.register(PageF,PageFAdmin)
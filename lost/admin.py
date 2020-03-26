from django.contrib import admin

# Register your models here.
from django.contrib import admin
from lost.models import KindL, PageL

class PageLAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

class KindLAdmin(admin.ModelAdmin):
    list_display = ('name','views', 'likes','slug')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(KindL,KindLAdmin)
admin.site.register(PageL,PageLAdmin)
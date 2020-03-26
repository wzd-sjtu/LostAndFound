from django.contrib import admin

# Register your models here.
from django.contrib import admin
from lost.models import KindL, PageL

admin.site.register(KindL)
admin.site.register(PageL)
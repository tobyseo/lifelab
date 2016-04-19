from django.contrib import admin
from .models import Point

class PointAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'created')
admin.site.register(Point, PointAdmin)

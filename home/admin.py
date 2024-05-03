from django.contrib import admin
from . import models
# Register your models here.
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('firstName',)
admin.site.register(models.Visitor, VisitorsAdmin)
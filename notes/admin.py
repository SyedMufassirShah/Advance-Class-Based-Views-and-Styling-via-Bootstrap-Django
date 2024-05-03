from django.contrib import admin
from . import models
# Register your models here.
class notesAdmin(admin.ModelAdmin):
    # this list_display is a Touple
    list_display = ('title',)  
admin.site.register(models.Note, notesAdmin)

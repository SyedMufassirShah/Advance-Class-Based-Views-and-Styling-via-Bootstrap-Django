from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Reminder
from django.http import Http404
from django.views.generic import ListView, DetailView

# Create your views here.
class ReminerListView(ListView):
    model =  Reminder
    template_name = 'reminder/reminders_list.html'
    context_object_name = 'reminders'

def display_reminder(request, pk):
    try:
        reminder = Reminder.objects.get(pk=pk)
    except Reminder.DoesNotExist:
        raise Http404("Page Does Not Exists!")
    return render(request, 'reminder/display_reminder.html', {'reminder' : reminder})

class DisplayReminderView(DetailView):
    model = Reminder
    template_name = 'reminder/display_reminder.html'
    context_object_name = 'reminder'

    def get_object(self, queryset = None):
        obj = super().get_object(queryset = queryset)
        if not obj:
            raise Http404("Page Does Not Exists!")
        return super().get_object(queryset)
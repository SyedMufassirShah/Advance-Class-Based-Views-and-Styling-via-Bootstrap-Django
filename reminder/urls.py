from django.urls import path
from . import views

urlpatterns = [
   path('', views.ReminerListView.as_view()), 
#    Add the Display Reminder View from views.py of Reminder
   path('Reminder/<int:pk>/', views.DisplayReminderView.as_view(), name = 'Reminder_Details'),
]

from django.urls import path
from . import views

# URLS
urlpatterns = [
    path('', views.NotesListView.as_view(), name='notes.list'),
    path('notes/<int:pk>/', views.DetailNotesView.as_view(), name='note_detail')
]

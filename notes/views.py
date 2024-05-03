from django.shortcuts import render
from .models import Note
from django.http import Http404
from django.views.generic import ListView,DetailView
# Create your views here.

# Previous Function Based View
# def noteslist(request):
#     all_Notes = Note.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes' : all_Notes })

# New Class Based View for the NoteList
class NotesListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

# Previous function Based View for the detial_note
# def detail(request,pk):
#     try:
#         note = Note.objects.get(pk = pk)
#     except Note.DoesNotExist:
#         raise Http404('This note does not Exists!')
#     return render(request, 'notes/detail_note.html', {'note' : note})


# New Class Based View for the detail_note
class DetailNotesView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = 'notes/detail_note.html' 
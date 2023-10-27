from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view()),
    path('notes/<int:pk>', views.NotesDetailView.as_view()),
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
]

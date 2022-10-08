from django.urls import path
from .import views

urlpatterns = [
    path('', views.NoteList.as_view(), name='note_list'),
    path('<int:pk>', views.NoteDetail.as_view(), name='note_view'),
    path('note_create', views.NoteCreate.as_view(), name='note_form'),
    path('<int:pk>/update', views.NoteUpdate.as_view(), name='note_update'),
    path('<int:pk>/note_delete', views.NoteDelete.as_view(), name='note_delete')
]

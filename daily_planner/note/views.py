from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note

from django.contrib.auth.mixins import LoginRequiredMixin


class NoteList(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = "note_list"

    def get_context_data(self, **kwargs):
        '''функция для спецификации данных и поиска заметок по названию'''
        context = super().get_context_data(**kwargs)
        context['note_list'] = context['note_list'].filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['note_list'] = context['note_list'].filter(
                note_tittle__icontains=search_input)  # поиск по заголовку
        context['search_input'] = search_input
        return context


class NoteDetail(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = 'note_view'
    template_name = 'note/note_view.html'


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = '__all__'
    template_name = 'note/note_form.html'
    success_url = reverse_lazy('note_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteUpdate, self).form_valid(form)


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    fields = '__all__'
    template_name = 'note/note_delete.html'
    success_url = reverse_lazy('note_list')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

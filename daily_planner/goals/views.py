from .models import Goal
from .forms import GoalForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class GoalList(LoginRequiredMixin, ListView):
    model = Goal
    context_object_name = "goal_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goal_list'] = context['goal_list'].filter(user=self.request.user)
        return context


class GoalDetailView(LoginRequiredMixin, DetailView):
    '''класс для обработки шаблона целей, для детального осмотра цели'''
    model = Goal
    template_name = 'goals/goals_view.html'
    context_object_name = 'goal'

# данная переменная в выступает в качестве ключа
class GoalUpdateView(LoginRequiredMixin, UpdateView):
    '''класс для редактиования имеющихся целей'''
    model = Goal
    # используется тот же самый шаблон, что и для добавления цели
    template_name = 'goals/goal_form.html'
    # передача в переменную form_class готовой формы для шаблона цели
    form_class = GoalForm


class GoalDeleteView(LoginRequiredMixin, DeleteView):
    '''класс для удаления долгосрочных целей'''
    model = Goal
    # ссылка для переадресации после удаления долгосрочной цели
    success_url = '/goals/'
    template_name = 'goals/goal_delete.html'

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


class GoalCreate(LoginRequiredMixin, CreateView):
    model = Goal
    template_name = 'goals/goal_form.html'
    form_class = GoalForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GoalCreate, self).form_valid(form)


# def add_goal(request):
#    '''функция для перехода в форму по добавлению целей, проверке корректности ввода данных цели и переадресации
#    при корректном вводеданных на страницу(redirect('home')) либо выводе ошибки при неккоректном вводе'''
#    error = ""
#    if request.method == "POST":
#        form = GoalForm(request.POST) # передаем в пост данные полученные от формы по добавлению
#        # проверка корректно ли заполнены данные и сохранение данных
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#        else:
#            error = "Форма была некоректно заполнена"
#
#    form = GoalForm
#    data = {
#        "form": form,
#        "error": error
#    }
#    return render(request, "goals/goal_form.html", data)

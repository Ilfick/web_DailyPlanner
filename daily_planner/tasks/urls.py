from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_view'),
    path('task_create', views.TaskCreate.as_view(), name='task_form'),
    path('task_update/<int:pk>/', views.TaskUpdate.as_view(), name='task_update'),
    path('<int:pk>/task_delete', views.TaskDelete.as_view(), name='task_delete')
]

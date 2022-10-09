from django.urls import path
from .import views

urlpatterns = [
    path('', views.GoalList.as_view(), name='goal_list'),
    path('add_goal', views.GoalCreate.as_view(), name='goal_form'),
    path('<int:pk>', views.GoalDetailView.as_view(), name='goal-detail'),
    path('<int:pk>/update', views.GoalUpdateView.as_view(), name='goal-update'),
    path('<int:pk>/delete', views.GoalDeleteView.as_view(), name='goal_delete')
]
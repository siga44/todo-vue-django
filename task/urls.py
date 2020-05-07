from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskView.as_view(), name="tasks_list_url"),
    path('<str:id>/complete/', views.TaskComplete.as_view()),
    path('<str:id>/delete/', views.TaskDelete.as_view())
]

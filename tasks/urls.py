from django.urls import path
from tasks.views import tasks_list, add_task, task_info, task_del, calendar

urlpatterns = [
    path('', tasks_list),
    path('add/', add_task),
    path('calendar/', calendar),
    path('info/<int:task_id>', task_info),
    path('<int:task_id>/del/', task_del),
]

from django.urls import path
from .views import (allApis, taskList, taskDetail,
                    taskCreate, taskUpdate, taskDelete) 

urlpatterns = [
    path('', allApis, name='home'),
    path('tasks/', taskList, name='tasks'),
    path('tasks/<str:pk>', taskDetail, name='task-detail'),
    path('create/', taskCreate, name='task-creat'),
    path('update/<str:pk>', taskUpdate, name='task-update'),
    path('delete/<str:pk>',taskDelete, name='task-delete')
]

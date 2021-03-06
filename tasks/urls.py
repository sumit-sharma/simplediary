"""simplediary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import TaskCreateFormView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create_task/', TaskCreateFormView.as_view(), name='task_create'),
    path('edit_task/<int:pk>', TaskUpdateView.as_view(), name='task_edit'),
    path('<pk>/delete/', TaskDeleteView.as_view()),
    path('download_csv', views.download_task_list, name='down_task_list_csv'),
]

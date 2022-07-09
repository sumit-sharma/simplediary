from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from tasks.models import Task

# from logging
# Create your views here.


@login_required
def home(request):
    task_count = Task.objects.count()
    context = {'pageName': 'Dashboard', 'task_count': task_count}
    return render(request, 'pages/home.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')

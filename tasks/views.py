from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Task
# Create your views here.

@login_required
def task_list(request):
    Tasks = Task.objects.all()
    paginator = Paginator(Tasks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'pages/task_list.html', context)
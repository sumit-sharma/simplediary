from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Task
from django.views.generic.edit import FormView, UpdateView
from .forms import TaskForm
# from django.urls import reverse

# Create your views here.


class TaskCreateFormView(FormView):
    model = Task
    template_name = 'task_form.html'
    form_class = TaskForm
    success_url = "/tasks"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    form_class = TaskForm
    success_url = "/tasks"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)






@login_required
def task_list(request):
    Tasks = Task.objects.all()
    paginator = Paginator(Tasks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'pages/task_list.html', context)


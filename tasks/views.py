from django.shortcuts import render
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
        task =  form.save(commit=False)
        task.created_by_id = self.request.user.id
        task.save()
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
    Tasks = Task.objects.all().filter(created_by_id=request.user.id)
    page_number = request.GET.get('page')
    work_status = request.GET.get('work_status')
    if(work_status):
        Tasks = Tasks.filter(work_status=work_status)

    paginator = Paginator(Tasks, 10)
    tasks = paginator.get_page(page_number)
    context = {'tasks': tasks}
    return render(request, 'pages/task_list.html', context)

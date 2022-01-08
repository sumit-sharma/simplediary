from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Task
from django.views.generic.edit import DeleteView, FormView, UpdateView
from .forms import TaskForm
import csv
import time
from django.db.models import Sum
from django.urls import reverse_lazy

# from django.urls import reverse

# Create your views here.


class TaskCreateFormView(FormView):
    model = Task
    template_name = "task_form.html"
    extra_context = {"pageName": "Create a Task"}
    form_class = TaskForm
    success_url = "/tasks"

    def form_valid(self, form):
        task = form.save(commit=False)
        task.created_by_id = self.request.user.id
        task.save()
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task_form.html"
    form_class = TaskForm
    success_url = "/tasks"
    extra_context = {"pageName": "Edit Task"}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# @login_required
class TaskDeleteView(DeleteView):
    model = Task
    
    success_url = "/tasks"
    # success_url = reverse_lazy('task_list')
    
    
    
    
    
    



@login_required
def task_list(request):
    Tasks = Task.objects.all().filter(created_by_id=request.user.id)
    page_number = request.GET.get("page")

    all_task_count = Tasks.count()
    # count total pending taks
    count_pending_work = Tasks.filter(work_status="pending").count()
    # sum of pending task amount
    total_pending_amount = Tasks.aggregate(
        Sum("pending_amount")
    )
    # count total pending taks
    advance_amount = Tasks.filter(work_status="pending").filter(
        amount_status="completed"
    )

    work_status = request.GET.get("work_status")
    if work_status:
        Tasks = Tasks.filter(work_status=work_status)
    amount_status = request.GET.get("amount_status")
    if amount_status:
        Tasks = Tasks.filter(amount_status=amount_status)
    
    start_date = request.GET.get("start_date")
    if start_date:
        Tasks = Tasks.filter(date__gte=start_date)
    end_date = request.GET.get("end_date")
    if end_date:
        Tasks = Tasks.filter(date__lte=end_date)



    paginator = Paginator(Tasks, per_page=25)
    tasks = paginator.get_page(page_number)
    context = {
        "tasks": tasks,
        "pageName": "Task List",
        "allTaskCount": all_task_count,
        "countPendingWork": count_pending_work,
        "totalPendingAmount": total_pending_amount,
        "advanceAmount": advance_amount,
    }
    return render(request, "pages/task_list.html", context)


@login_required
def download_task_list(request):
    response = HttpResponse(
        content_type="text/csv",
        headers={
            "Content-Disposition": 'attachment; filename="sa_'
            + str(time.time())
            + '.csv"'
        },
    )
    Tasks = Task.objects.all().filter(created_by_id=request.user.id)
    work_status = request.GET.get("work_status")
    if work_status:
        Tasks = Tasks.filter(work_status=work_status)

    start_date = request.GET.get("start_date")
    if start_date:
        Tasks = Tasks.filter(date__gte=start_date)
    end_date = request.GET.get("end_date")
    if end_date:
        Tasks = Tasks.filter(date__lte=end_date)


    # page_number = request.GET.get('page')
    # paginator = Paginator(Tasks, 10)
    # tasks = paginator.get_page(page_number)

    writer = csv.writer(response)
    writer.writerow(["Date", "Customer Name", "Contact Details", "Description", "Work status", "Amount", "Total amount", "Advance amount", "Pending amount", "Remark"])
    tsks = Tasks.values_list("date","customer_name", "contact_details", "description", "work_status", "amount_status", "total_amount", "advance_amount", "pending_amount", "remark")
    for tsk in tsks:
        writer.writerow(tsk)
    return response

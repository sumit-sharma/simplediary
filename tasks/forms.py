from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        fields = (
            "date",
            "customer_name",
            "contact_details",
            "description",
            "work_status",
            "amount_status",
            "total_amount",
            "advance_amount",
            "pending_amount",
            "remark",
        )

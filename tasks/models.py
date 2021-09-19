from django.db import models
from datetime import datetime

# specify transaction_type
STATUS_CHOICES = (
    ("pending", "pending"),
    ("completed", "completed"),
)

# Create your models here.


class Task(models.Model):
    date = models.DateField(default=datetime.today)
    customer_name = models.CharField(max_length=225)
    contact_details = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)
    work_status = models.CharField(max_length=225, default = "pending",  choices=STATUS_CHOICES)
    amount_status = models.CharField(default = "pending", max_length=225, choices=STATUS_CHOICES)
    Total_amount = models.PositiveBigIntegerField()
    advance_amount = models.PositiveBigIntegerField()
    pending_amount = models.PositiveBigIntegerField()
    remark = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "tasks"

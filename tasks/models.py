from django.contrib.auth.models import User
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
    created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=225)
    contact_details = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)
    work_status = models.CharField(
        max_length=225, default="pending", choices=STATUS_CHOICES)
    amount_status = models.CharField(
        default="pending", max_length=225, choices=STATUS_CHOICES)
    total_amount = models.PositiveBigIntegerField()
    advance_amount = models.PositiveBigIntegerField()
    pending_amount = models.PositiveBigIntegerField()
    remark = models.TextField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "tasks"
        ordering = ['-id']

    def __str__(self): 
        return self.customer_name 

    
    
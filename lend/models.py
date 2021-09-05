from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Borrower(models.Model):
    name = models.CharField(max_length=225)
    nick_name = models.CharField(max_length=225)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by")
    remind_me_at = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "borrowers"



# specify transaction_type
TRANSACTION_CHOICES = (
    (1, "credit"),
    (2, "debit"),
)

class Transaction(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    transaction_type = models.CharField(
                        max_length=50,
                        choices= TRANSACTION_CHOICES,
                    )
    remark = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField("created at", default=timezone.now)

    class Meta:
        db_table = "transactions"




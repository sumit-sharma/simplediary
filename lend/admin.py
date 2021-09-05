from django.contrib import admin

# Register your models here.
from .models import Borrower, Transaction


admin.site.register(Borrower)
admin.site.register(Transaction)
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse

# Register your models here.
from .models import Borrower, Transaction


class BorrowerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "nick_name", "transaction_link"]

    def transaction_link(self, request):
        url = reverse("admin:lend_transaction_changelist")
        url += "?borrower__id="+str(request.id)
        link = '<a href="%s">%s</a>' % (url, "Transaction")
        return mark_safe(link)

    transaction_link.short_description = 'show transaction'

class TransactionAdmin(admin.ModelAdmin):
    
    def created_date(self, obj):
        return obj.created_at.strftime("%d %b %Y %I:%M %p")
    
    list_display = ["borrower_name", "amount", "transaction_type", "created_date"]

    list_filter = ('borrower__name', 'created_at',)

    search_fields = ["borrower__name", "amount", "transaction_type"]


    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     queryset = queryset.annotate(
    #         # _borrowerName=request.select_related("borrower"),
    #         _borrowerName=self.borrower.name,
    #         # _borrower_nickname=obj.borrower.name
    #     )
    #     return queryset

    # def borrower_name(self, obj):
    #     return obj._borrowerName

    # def borrower_nickname(self, obj):
    #     return obj._borrower_nickname


    def borrower_name(self, object):
        return object.borrower.name

    def borrower_nickname(object):
        return object.borrower.nick_name


admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(Transaction, TransactionAdmin)

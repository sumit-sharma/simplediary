from django.contrib import admin

# Register your models here.
from .models import Product, Price


class PriceAdmin(admin.ModelAdmin):
    def created_date(self, obj):
        return obj.created_at.strftime("%d %b %Y")

    list_display = ("amount", "product", "created_date")


admin.site.register(Product)
admin.site.register(Price, PriceAdmin)
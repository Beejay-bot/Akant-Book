from django.contrib import admin
from .models import *

# Register your models here.
class Business_AcctConfig(admin.ModelAdmin):
    list_display = ['user', 'business_name', 'Type_of_service', 'business_email_address']
    search_fields = ['user', 'business_name', 'business_email_address']
    list_filter = ['Type_of_service', 'user']

class ImportConfig(admin.ModelAdmin):
    list_display = ['business', 'income_type', 'amount', 'Date_added']
    search_fields = ['business', 'income_type']
    list_filter = ['business','Date_added', 'income_type']


class ExpenseConfig(admin.ModelAdmin):
    list_display = ['business', 'Type', 'amount', 'payment_method', 'Date_added']
    search_fields = ['business', 'Type', 'payment_method']
    list_filter = ['business','Date_added', 'Type', 'payment_method']


admin.site.register(Business_Account, Business_AcctConfig)
admin.site.register(Expenses, ExpenseConfig)
admin.site.register(Income, ImportConfig)
admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.register(Product)

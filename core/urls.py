from django.urls import path
from .views import *

urlpatterns = [
    path("", indexView, name="home"),
    path('register-business', businessAcctFormView, name='register-business'),
    path('dashboard', dashboardView, name='dashboard'),
    path('expenses', expenseView, name='expenses'),
    path('add-expenses', addExpenseView, name='add-expenses'),
    path('income', incomeView, name='income'),
    path('add-income', addIncomeView, name='add-income'),
    # path("delete-customers/<slug>", deleteCustomer, name='delete-customer'),
    path('add-customer', addCustomerView, name='add-customer'),
    path('customers', customerView, name='customers'),
    path('customers/<slug>', customerDetails, name='customerDetails'),
    path('add-transaction', TransactionView, name='add-transaction'),
]

from django.urls import path
from .views import *


urlpatterns=[
    path("", indexView, name="home"),
    path('register-business', businessAcctFormView, name='register-business'),
    path('dashboard', dashboardView, name='dashboard'),
    path('expenses', expenseView, name='expenses'),
    path('income', incomeView, name='income'),
    path('add-income', addIncomeView, name='add-income'),
    path('add-customers', customerView, name='add-customer'),
    path('customers', customerView, name='customers'),
    path('add-transaction', TransactionView, name='add-transaction'),
]
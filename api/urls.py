from core.models import Income
from django.urls import path
from .views import AddBusinessAcctView,DeleteBusinessAcctView, CustomerView,EditCustomerView, DeleteExpenseView, DeleteIncomeView, ExpensesView, IncomeView, TransactionView

urlpatterns = [
    path('business_account/', AddBusinessAcctView.as_view(), name='Business_accounts'),
    path('delete_business_account/<int:pk>/', DeleteBusinessAcctView.as_view(), name='delete_business_accounts'),
    path('expenses/<int:business>/', ExpensesView.as_view(), name='expensesApi'),
    path('delete_expense/<int:pk>/', DeleteExpenseView.as_view(), name='delete_expense'),
    path('income/<int:business>/', IncomeView.as_view(), name='income_view'),
    path('delete_income/<int:pk>/', DeleteIncomeView.as_view(), name='delete_income'),
    path('customers/<int:business>/', CustomerView.as_view(), name='customer_view'),
    path('edit_customer/<int:pk>/', EditCustomerView.as_view(), name='delete_income'),
    path('transaction/<int:business>/', TransactionView.as_view(), name='transaction')
]

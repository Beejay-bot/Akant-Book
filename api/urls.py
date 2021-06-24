from django.urls import path
from .views import AddBusinessAcctView, DeleteExpenseView, ExpensesView

urlpatterns = [
    path('business_accounts/', AddBusinessAcctView.as_view(), name='Business_accounts'),
    path('expenses/', ExpensesView.as_view(), name='expensesApi'),
    path('expense/<int:pk>/', DeleteExpenseView.as_view(), name='delete_expense')
]

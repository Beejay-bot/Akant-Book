from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import message
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import *

from .models import *


# Create your views here.

def indexView(request):
    return render(request, 'home.html')


def businessAcctFormView(request):
    if request.method == 'POST':
        businessName = request.POST['Business_name']
        TypeOfService = request.POST['Type_of_service']
        emailBusiness = request.POST['business_email_address']

        if Business_Account.objects.filter(business_name=businessName).exists():
            messages.info(request, 'Sorry this Business name already exists')
            return redirect('register-business')
        elif Business_Account.objects.filter(business_email_address=emailBusiness).exists():
            messages.info(request, 'Sorry this email is already taken')
            return redirect('register-business')
        else:
            business = Business_Account.objects.create(business_name=businessName, Type_of_service=TypeOfService,
                                                       business_email_address=emailBusiness)
            business.save()
            print('Business Created')
            return redirect('dashboard')
    return redirect('dashboard')


def dashboardView(request):
    return render(request, 'dashboard.html')


def expenseView(request):
    form = ExpensesForm(request.POST)
    if form.is_valid():
        expense_type = form.cleaned_data.get('expense_type')
        amount = form.cleaned_data.get('amount')
        note = form.cleaned_data.get('note')

        expense = Expenses()
        expense.Type = expense_type
        expense.amount = amount
        expense.Notes = note
        expense.save()
        messages.success(request, 'Expense Added')
        redirect('dashboard')

    form = ExpensesForm()
    expenses_form = Expenses.objects.all()
    context = {
        'form': form,
        'expenses_form': expenses_form
    }
    return render(request, 'expense.html', context)


def incomeView(request):
    income_form = Income.objects.all()
    context = {
        'income_form': income_form
    }
    return render(request, 'income.html', context)


def addIncomeView(request):
    form = IncomeForm(request.POST)
    if form.is_valid():
        income_type = form.cleaned_data.get('income_type')
        amount = form.cleaned_data.get('amount')
        note = form.cleaned_data.get('note')

        income = Income()
        income.income_type = income_type
        income.amount = amount
        income.Notes = note
        income.save()
        messages.success(request, 'Expense Added')
        return redirect('income')
    form = IncomeForm()
    context = {
        'form': form}
    return render(request, 'addincome.html', context)


def customerView(request):
    pass


def TransactionView(request, id):
    form = TransactionForm(request.POST)
    if form.is_valid():
        customer = form.cleaned_data.get('customer')
        amount = form.cleaned_data.get('amount')
        reference = form.cleaned_data.get('reference')

        try:
            transaction = Transaction()
            transaction.customer = customer
            transaction.amount = amount
            transaction.reference_note = reference
            transaction.save()
        except ObjectDoesNotExist:
            messages.info(request, 'Uhhhn, Something went wrong, please try again.')
    else:
        transaction = Transaction.objects.get(pk=id)
        form = TransactionForm(instance=transaction)

    transaction_form = TransactionForm()
    transactions = Transaction.objects.all()
    context = {
        'form': transaction_form,
        'transactions': transactions,
        'forms': form
    }

    return render(request, 'transaction.html', context)

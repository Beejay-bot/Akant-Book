from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import message
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required

from .forms import *

from .models import *


# Create your views here.

def indexView(request):
    return render(request, 'home.html')


@login_required
def businessAcctFormView(request):
    if request.method == 'POST':
        business = Business_Account.objects.get(user=request.user)
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


@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')


@login_required
def expenseView(request):
    expenses_form = Expenses.objects.all()
    context = {
        'expenses_form': expenses_form
    }
    return render(request, 'expense.html', context)


def addExpenseView(request):
    form = ExpensesForm(request.POST)
    admin = Expenses.objects.filter(user=request.user)
    if form.is_valid():
        expense_type = form.cleaned_data.get('expense_type')
        amount = form.cleaned_data.get('amount')
        note = form.cleaned_data.get('note')

        expense = Expenses()
        expense.user = request.user
        expense.Type = expense_type
        expense.amount = amount
        expense.Notes = note
        expense.save()
        messages.success(request, 'Expense Added')
        return redirect('expenses')
    form = ExpensesForm()
    context = {
        'form': form,
    }
    return render(request, 'addexpense.html', context)


def incomeView(request):
    income_form = Income.objects.all()
    context = {
        'income_form': income_form
    }
    return render(request, 'income.html', context)


def addIncomeView(request):
    form = IncomeForm(request.POST)
    admin = Income.objects.filter(user=request.user)
    if form.is_valid():
        income_type = form.cleaned_data.get('income_type')
        amount = form.cleaned_data.get('amount')
        note = form.cleaned_data.get('note')

        income = Income()
        income.administrator = request.user
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
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'customer.html', context)


def addCustomerView(request):
    form = CustomerForm(request.POST)
    if form.is_valid():
        customer_name = form.cleaned_data.get('customer_name')
        customer_phone_number = form.cleaned_data.get('customer_phone_number')
        customer_email = form.cleaned_data.get('customer_email')
        Description = form.cleaned_data.get('Description')

        customer = Customer()
        customer.customer_name = customer_name
        customer.customer_phone_number = customer_phone_number
        customer.email = customer_email
        customer.Description = Description
        customer.save()
        messages.success(request, 'Customer successfully added.')
        return redirect('customers')
    form = CustomerForm()
    context = {
        'form': form}
    return render(request, 'addcustomer.html', context)


def customerDetails(request):
    context = {
        'customers': Customer.objects.all()
    }
    return render(request, 'customerdetails.html', context)


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


def deleteIncome(request, my_id):
    income = get_object_or_404(Income, pk=my_id)
    income_qs = Income.objects.filter()

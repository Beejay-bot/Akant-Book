from django import forms
from .models import *

EXPENSE_CATEGORY = (
    ('Tax', 'Tax'),
    ('Electricity', 'Electricity'),
    ('Transportation', 'Transportation'),
    ('Rent', 'Rent'),
    ('Raw Materials', 'Raw Materials'),
    ('Salary', 'Salary'),
    ('Loan', 'Loan'),
    ('Insurance', 'Insurance'),
    ('Maintenance & Repairs', 'Maintenance & Repairs'),
    ('Miscellaneous', 'Miscellaneous')
)

INCOME_CATEGORY = (
    ('Profit', 'Profit'),
    ('Rentals', 'Rentals'),
    ('Sales', 'Sales'),
    ('Dividend', 'Dividend'),
    ('Investments', 'Investments'),
    ('Donations', 'Donations'),
)


class ExpensesForm(forms.Form):
    expense_type = forms.ChoiceField(widget=forms.Select(attrs={
        'class': ' form-group custom-select mb-3'
    }), choices=EXPENSE_CATEGORY)
    amount = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Amount'}))
    note = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control mb-3',
        'rows': 3
    }))


class IncomeForm(forms.Form):
    income_type = forms.ChoiceField(widget=forms.Select(attrs={
        'class': ' form-group custom-select mb-3'
    }), choices=INCOME_CATEGORY)
    amount = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Amount'}))
    note = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control mb-3',
        'rows': 3
    }))


class CustomerForm(forms.Form):
    customer_name = forms.CharField(max_length=100, required=True)
    customer_phone_number = forms.CharField(max_length=15, required=True)
    customer_email = forms.EmailField(required=True)
    Description = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))


class TransactionForm(forms.Form):
    class Meta:
        model = Transaction

    def __init__(self, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        user = kwargs.pop('user', '')
        self.fields['customer'] = forms.ModelChoiceField(queryset=Transaction.objects.filter(customer=user))

    amount = forms.FloatField(required=True)
    reference = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))

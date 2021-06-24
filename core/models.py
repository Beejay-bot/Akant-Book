from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()

SERVICE_CATEGORIES = (
    ('Goods', 'Goods'),
    ('Services', 'Services')
)

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


class Business_Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=50)
    Type_of_service = models.CharField(choices=SERVICE_CATEGORIES, max_length=50)
    business_email_address = models.EmailField(max_length=254)

    class Meta:
        verbose_name = "Business_Account"
        verbose_name_plural = "Business_Accounts"

    def __str__(self):
        return self.business_name


class Expenses(models.Model):
    business = models.ForeignKey(Business_Account, on_delete=models.CASCADE)
    Type = models.CharField(choices=EXPENSE_CATEGORY, max_length=50)
    amount = models.FloatField()
    Date_added = models.DateTimeField(auto_now_add=True)
    Notes = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    def __str__(self):
        return f'{self.Type} expense for {self.business}'


class Income(models.Model):
    business = models.ForeignKey(Business_Account, on_delete=models.CASCADE)
    income_type = models.CharField(choices=INCOME_CATEGORY, max_length=50)
    amount = models.FloatField()
    Date_added = models.DateTimeField(auto_now_add=True)
    Notes = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Income"
        verbose_name_plural = "Income"

    def __str__(self):
        return f'{self.income_type} income for  {self.business}'

    def get_absolute_url(self):
        return reverse("Business_Account_detail", kwargs={"pk": self.pk})


class Customer(models.Model):
    user = models.ForeignKey(Business_Account, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phone_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    Description = models.TextField(max_length=500)
    slug = models.SlugField(unique=True,)

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse("customerDetails", kwargs={"slug": self.slug})


class Transaction(models.Model):
    user = models.ForeignKey(Business_Account, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.FloatField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    reference_note = models.TextField(max_length=250)

    def __str__(self):
        return self.customer

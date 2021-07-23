import re
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from rest_framework import status

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
    ('Utilities','Utilities'),
    ('Savings', 'Savings'),
    ('Maintenance & Repairs', 'Maintenance & Repairs'),
    ('Miscellaneous', 'Miscellaneous')
)

INCOME_CATEGORY = (
    ('Profit', 'Profit'),
    ('Rentals', 'Rentals'),
    ('Sales', 'Sales'),
    ('Dividend', 'Dividend'),
    ('Loan', 'Loan'),
    ('Investments', 'Investments'),
    ('Donations', 'Donations'),
)

PAYMENT_METHOD = (
    ('CASH','CASH'),
    ('POS','POS'),
    ('TRANSFER','TRANSFER'),
    ('CREDIT','CREDIT')
)

class Business_Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=50, blank=False)
    Type_of_service = models.CharField(choices=SERVICE_CATEGORIES, max_length=50)
    business_email_address = models.EmailField(max_length=254, blank=True)

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
    Notes = models.TextField(max_length=500, blank=True)
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=50)

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
    Notes = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = "Income"
        verbose_name_plural = "Income"

    def __str__(self):
        return f'{self.income_type} income for  {self.business}'


class Customer(models.Model):
    business = models.ForeignKey(Business_Account, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phone_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    Description = models.TextField(max_length=500)

    def __str__(self):
        return self.customer_name


class Product(models.Model):
    business = models.ForeignKey(Business_Account, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    image = models.ImageField(upload_to=None)
    current_product_stock_available =  models.IntegerField()

    def __str__(self):
        return self.product_name



generate_ref_no = str(uuid.uuid1())

class Transaction(models.Model):
    business = models.ForeignKey(Business_Account, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    productSold = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quanties_of_product_sold = models.IntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=50)
    reference_num = models.CharField(max_length=50, editable=False, default=generate_ref_no, unique=True)

    def __str__(self):
        return f'{self.customer} '

    def get_quantities_sold(self,quantities_sold):
        return print(quantities_sold)
    
    
    def can_reduce_product_quanity(self, quantityToBeRemoved,ProductObj):
        amount = int(quantityToBeRemoved)
        return ProductObj.current_product_stock_available >= amount
    
    def deduct_quanity(self,quantity, ProductObj):
        if self.can_reduce_product_quanity(quantity, ProductObj):
            amount = int(quantity)
            ProductObj.current_product_stock_available -= amount
            ProductObj.save()
            self.save()
            return {'Message':f"{quantity} {ProductObj.product_name} has been deducted from {ProductObj.product_name}'s available stock", 'Remainder':f"You have {ProductObj.current_product_stock_available} remaining {ProductObj.product_name} left","Status":status.HTTP_200_OK}
        return {'Message':f"sorry we couldn't deduct the quantity of product sold has {ProductObj.product_name} remains {ProductObj.current_product_stock_available}. Please update the remaining stock available for this product.", 'Status':status.HTTP_404_NOT_FOUND}

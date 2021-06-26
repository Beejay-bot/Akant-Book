from django.db import models
from django.db.models import fields
from rest_framework import serializers
from core.models import Business_Account, Customer, Expenses, Income, Transaction


class BusinessAcctSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business_Account
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = "__all__"
class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from core.models import Business_Account, Expenses


class BusinessAcctSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business_Account
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = "__all__"
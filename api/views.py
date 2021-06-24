from django.db import models
from django.db.models import query
from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.views import APIView
from core.models import Business_Account, Expenses, User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import BusinessAcctSerializer, ExpenseSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class AddBusinessAcctView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Business_Account.objects.all()
    serializer_class = BusinessAcctSerializer


class ExpensesView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer

class DeleteExpenseView(generics.RetrieveDestroyAPIView):
    permission_classes= [IsAuthenticated]
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer
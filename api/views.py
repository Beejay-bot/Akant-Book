from django.db import models
from django.db.models import manager, query
from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework import response
from rest_framework.views import APIView
from core.models import Business_Account, Customer, Expenses, Income, User
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import BusinessAcctSerializer, CustomerSerializer, ExpenseSerializer, IncomeSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class AddBusinessAcctView(APIView):
    def get_object(self):
        try:
            return Business_Account.objects.all()
        except:
            raise status.HTTP_404_NOT_FOUND

    def get(self,request):
        queryset = self.get_object()
        serializer = BusinessAcctSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = BusinessAcctSerializer(data=request.data)
        try:
            if serializer.is_valid():
                print(serializer.validated_data)
                if Business_Account.objects.filter(business_name=serializer.validated_data['business_name']).exists():
                    return Response(data={'message':'This business already exists'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                elif Business_Account.objects.filter(business_email_address = serializer.validated_data['business_email_address']).exists():
                    return Response(data={'message':'Please trying another email, this email is used by a business'}, status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(data=serializer.error_messages, status=status.HTTP_404_NOT_FOUND)


class ExpensesView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer

class DeleteExpenseView(generics.DestroyAPIView):
    permission_classes= [IsAuthenticated]
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer


class IncomeView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class DeleteIncomeView(generics.DestroyAPIView):
    permission_classes= [IsAuthenticated]
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class CustomerView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class EditCustomerView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes= [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


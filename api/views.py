from rest_framework import generics
from rest_framework.views import APIView
from core.models import Business_Account, Customer, Expenses, Income, Product, Transaction
from rest_framework.permissions import IsAuthenticated
from .serializer import BusinessAcctSerializer, CustomerSerializer, ExpenseSerializer, IncomeSerializer, TransactionSerializer
from rest_framework.response import Response
from rest_framework import status
from .Permissions import AuthorityToMakeRequestForAParticularBusiness
import json

# Create your views here.


class AddBusinessAcctView(APIView):
    def get_object(self,request):
        try:
            return Business_Account.objects.filter(user=request.user)
        except:
            raise status.HTTP_404_NOT_FOUND

    def get(self,request):
        queryset = self.get_object(request)
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
            return Response(data=serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

class DeleteBusinessAcctView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Business_Account.objects.all()
    serializer_class = BusinessAcctSerializer

class ExpensesView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, AuthorityToMakeRequestForAParticularBusiness]
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer

    def get(self, request, business=None, *args, **kwargs):
        query = Expenses.objects.filter(business=business)
        Serializer = self.serializer_class(instance=query, many=True)
        return Response(data=Serializer.data, status=status.HTTP_200_OK)

class DeleteExpenseView(generics.DestroyAPIView):
    permission_classes= [IsAuthenticated]
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializer


class IncomeView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, AuthorityToMakeRequestForAParticularBusiness]
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def get(self, request,business=None):
        query = Income.objects.filter(business=business)
        serializer =self.serializer_class(query, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class DeleteIncomeView(generics.DestroyAPIView):
    permission_classes= [IsAuthenticated]
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class CustomerView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request,business=None):
        query = Income.objects.filter(business=business)
        serializer =self.serializer_class(query, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class EditCustomerView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes= [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class TransactionView(APIView):
    def get(self,request):
        query = Transaction.objects.all()
        
        print(request.user)
        serializer = TransactionSerializer(query, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
                print(serializer.data['quanties_of_product_sold'])
                # Product.deduct_quanity(self,serializer.data['quanties_of_product_sold']) #deduct the quantities sold from the particular product in stock.
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)
    



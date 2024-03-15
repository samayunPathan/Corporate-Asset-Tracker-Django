from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .models import *
from .serializers import *


# this class view for List all Companys, or create a new instence 
class CompanyListCreateView(viewsets.ModelViewSet):
    queryset=CompanyModel.objects.all()
    serializer_class=CompanySerializer



# this class view for List all employee , or create a new instence 
class EmployeeListCreateView(viewsets.ModelViewSet):
    queryset=EmployeeModel.objects.all()
    serializer_class=EmployeeSerializer
    


# this class view for List all asstes , or create a new instence 
class AssetsListCreateView(viewsets.ModelViewSet):
    queryset=AssetsModel.objects.all()
    serializer_class=AssetsSerializer

   


# this class view for Retrieve, update or delete a assets instance.
class AssetslogView(viewsets.ModelViewSet):
    queryset=AssetsLog.objects.all()
    serializer_class=AssetsLogSerializer
    
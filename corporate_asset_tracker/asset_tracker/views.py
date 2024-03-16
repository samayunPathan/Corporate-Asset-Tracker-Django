from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import *
from .models import *
from .serializers import *


# this class view for List all Companys, or create a new instence 
class CompanyListCreateView(viewsets.ModelViewSet):
    queryset=CompanyModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class=CompanySerializer



# this class view for List all employee , or create a new instence 
class EmployeeListCreateView(viewsets.ModelViewSet):
    queryset=EmployeeModel.objects.all()
    # permission_classes = (IsAuthenticated,IsAdminUser)
    serializer_class=EmployeeSerializer
    


# this class view for List all asstes , or create a new instence 
class AssetsListCreateView(viewsets.ModelViewSet):
    queryset=AssetsModel.objects.all()
    serializer_class=AssetsSerializer
    # permission_classes = (IsAuthenticated,)

   


# this class view for Retrieve, update or delete a assets instance.
class AssetslogView(viewsets.ModelViewSet):
    queryset=AssetsLog.objects.all()
    serializer_class=AssetsLogSerializer
    # permission_classes = (IsAuthenticated,IsAdminUser)
    
from rest_framework import serializers
from .models import *

# serialisers to clean and formate data 
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsModel
        fields = '__all__'

class AssetsLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsLog
        fields = '__all__'


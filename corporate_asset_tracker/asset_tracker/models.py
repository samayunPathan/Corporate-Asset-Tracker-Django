from django.db import models
from django.utils import timezone

# Create your models here.

# for company table to register company 
class CompanyModel(models.Model):
   company_name = models.CharField(max_length=100)
   def __str__(self):
      return self.company_name

# employee table linked to the company table to register their employee 
class EmployeeModel(models.Model):
   company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)
   employee_name = models.CharField(max_length=100)
   employee_department = models.CharField(max_length=100)
   
   def __str__(self):
      return self.employee_name


# assets table to register all device which will delegate  
class AssetsModel(models.Model):
   asset_name = models.CharField(max_length=100)
   asset_manufacturer = models.CharField(max_length=100)
   asset_purchased_date = models.DateTimeField(default=timezone.now)
   asset_condition = models.TextField()
   asset_issued = models.BooleanField(default=False)
   
   class Meta:
      ordering = ['asset_purchased_date']
   
   def __str__(self):
      return self.asset_name + " "+ self.asset_manufacturer


# a table to track the asset check out and check in 
class AssetsLog(models.Model):
   asset = models.ForeignKey(AssetsModel, on_delete=models.CASCADE, null=True, blank=True)
   employee = models.ForeignKey(EmployeeModel,  on_delete=models.CASCADE, null=True, blank=True)
   checkout_date = models.DateTimeField()
   return_date = models.DateTimeField(null=True, blank=True)
   checkout_condition = models.TextField()
   return_condition = models.TextField(null=True, blank=True)

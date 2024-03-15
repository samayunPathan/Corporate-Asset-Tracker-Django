from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

app_name='asset_tracker'
router=DefaultRouter()

router.register(r'company',CompanyListCreateView,basename='company')
router.register(r'employee',EmployeeListCreateView,basename='employee')
router.register(r'asset',AssetsListCreateView,basename='asset')
router.register(r'assetlog',AssetslogView,basename='assetlog')
router.register(r'assetlog/<id>',AssetslogView,basename='assetlog')



urlpatterns = []+router.urls

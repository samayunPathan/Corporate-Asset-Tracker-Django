from django.urls import path
from asset_tracker import views

app_name='asset_tracker'

urlpatterns = [
    path('',views.asset,name='datetime')
]

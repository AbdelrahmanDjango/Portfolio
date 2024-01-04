from django.urls import path, include
from .views import show_my
app_name = 'MyJob'

urlpatterns = [
    path('', show_my), 
]
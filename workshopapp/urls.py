from django.urls import path
from workshopapp.views import *

urlpatterns = [
    path('', index_page)
]

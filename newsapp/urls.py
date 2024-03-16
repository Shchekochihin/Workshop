from django.urls import path
from newsapp.views import *

urlpatterns = [
    path('<int:newsid>/', news_page)
]
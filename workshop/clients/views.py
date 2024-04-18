from django.http import HttpResponse
from .models import *


def index(request):
    client = Clients.objects.get(id=1)
    return HttpResponse("Hello {}".format(client.first_name))

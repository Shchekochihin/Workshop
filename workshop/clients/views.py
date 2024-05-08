from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Clients


def index(request):
    return render(request, 'clients/index.html')


def client(request, client_id):
    client = get_object_or_404(Clients, pk=client_id)
    data = {
        'title': client.first_name + ' ' + client.last_name,
        'client': client
    }
    return render(request, 'clients/client.html', data)

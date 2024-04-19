from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = {'title':'Hello World'}
    return render(request, 'clients/index.html', data)


def client(request, client_id):
    return HttpResponse(f"Hello client {client_id}")

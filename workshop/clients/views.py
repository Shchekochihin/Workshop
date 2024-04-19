from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello {}")


def client(request, client_id):
    return HttpResponse(f"Hello client {client_id}")

from django.http import HttpResponse
from django.shortcuts import render

def news_page(request, newsid):
    return HttpResponse(f"<h1>news page</h1><p>{newsid}</p>")

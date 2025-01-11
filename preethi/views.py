from django.shortcuts import render
from django.http import HttpResponse

def req_obj(request):
    return render(request, "preethish.html")


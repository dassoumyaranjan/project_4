from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return HttpResponse('hai This app1 Dhoni s page')

def rohit(request):
    return HttpResponse('Rohit The HiTmanN')

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
def index(request):
    # return HttpResponse('hello world')
    tk=tasks.objects.all()
    context={'tk':tk}
    return render(request, 'list.html', context)
# Create your views here.

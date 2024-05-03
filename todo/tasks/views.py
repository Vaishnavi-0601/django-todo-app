from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

from .forms import *




def index(request):
    # return HttpResponse('hello world')
    tk=tasks.objects.all()
    form=taskforms()

    if request.method=='POST':
        form=taskforms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')



    context={'tk':tk, 'form':form}
    return render(request, 'list.html', context)
# Create your views here.

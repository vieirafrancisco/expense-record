from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def register(request):
    error_message = ''
    if request.POST:
        try:
            args = {key:value for key, value in request.POST.items() if 'csrf' not in key}
            user = User(**args)
            user.save()
        except Exception as e:
            error_message = e
        else:
            return HttpResponseRedirect('main_app/index.html', 
                                        {'username': request.POST['username']})
    return render(request, 'main_app/register.html', {'error_message': error_message})

def login(request):
    return HttpResponse("Hello Login!")
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main_app:dashboard', args=(request.user.id,)))
    return render(request, 'main_app/index.html')

@login_required
def dashboard(request, user_id):
    user = request.user
    if not user.is_authenticated or user_id != user.id:
        raise Http404("User not logged in!")
    return render(request, 'main_app/dashboard.html', {'user': user})

def login_view(request):
    error_message = ''
    if request.POST:
        args = request.POST
        user = authenticate(request, username=args['username'], password=args['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
            return HttpResponseRedirect(reverse('main_app:dashboard', args=(user.id,)))
        error_message = "User doesn't exist!"
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main_app:dashboard', args=(request.user.id,)))
    return render(request, 'main_app/login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main_app:index'))

def register(request):
    error_message = ''
    if request.POST:
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            # TODO need to make login before creating the user
            # redirect to login_view?
            login(request, user)
        except Exception as e:
            error_message = e
        else:
            return HttpResponseRedirect(reverse('main_app:dashboard', args=(user.id,)))
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main_app:dashboard', args=(request.user.id,)))
    return render(request, 'main_app/register.html', {'error_message': error_message})
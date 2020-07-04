from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.urls import reverse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main_app:dashboard', args=(request.user.id,)))
    return render(request, 'main_app/index.html')

@login_required
def dashboard(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if not user.is_authenticated:
        return Http404("User not logged in!")
    return render(request, 'main_app/dashboard.html', {'user': user})

def login(request):
    error_message = ''
    if request.POST:
        args = request.POST
        user = authenticate(request, username=args['username'], password=args['password'])
        if user is not None:
            if user.is_active:
                request.session.set_expiry(86400)
                auth_login(request, user)
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
            args = {key:value for key, value in request.POST.items() if 'csrf' not in key}
            user = User(**args)
        except Exception as e:
            error_message = e
        else:
            user.save()
            return HttpResponseRedirect(reverse('main_app:dashboard', args=(user.id,)))
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main_app:dashboard', args=(request.user.id,)))
    return render(request, 'main_app/register.html', {'error_message': error_message})
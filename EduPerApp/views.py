from django.shortcuts import render, get_object_or_404, redirect
from .forms import SignUpForm
# Create your views here.
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib import messages


def Home(request):
    context = {}
    return render(request, 'index.html', context)


def Register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password_raw = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password_raw)
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Your new and reset password is not matching")
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Your username or password is invalid.')
    context = {}
    return render(request, 'Login.html', context)

from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User = get_user_model()
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            messages.success(request, "Thank you for registering. You can now login.")
            return redirect('accounts:dashboard')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=identifier, password=password)
            if user is None:
                User = get_user_model()
                try:
                    candidate = User.objects.get(username=identifier, password=password)
                except User.DoesNotExist:
                    candidate = None
                if candidate is not None:
                    user = authenticate(request, username=candidate.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You are now logged in.")
                return redirect('accounts:dashboard')
            form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_success_view(request):
    return  redirect('accounts:register_success')

def dashboard_view(request):
    return render(
        request,
        'accounts/dashboard.html',
        {'active_user': request.session.get('active_user','Guest')},
    )
@login_required
def logout_view(request):
    if request.method != "POST":
        return redirect('accounts:dashboard')
    logout(request)
    messages.info(request, "You are now logged out.")
    return redirect('home')
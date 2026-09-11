from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# pyrefly: ignore [missing-import]
from .forms import RegisterForm
# pyrefly: ignore [missing-import]
from .models import UserProfile


def home(request):
    return render(request, 'home.html')


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        return render(
            request,
            'accounts/login.html',
            {
                'error': 'Invalid username or password'
            }
        )

    return render(
        request,
        'accounts/login.html'
    )


@login_required
def dashboard(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    return render(
        request,
        'accounts/dashboard.html',
        {
            'profile': profile
        }
    )


def logout_view(request):

    logout(request)

    return redirect('login')
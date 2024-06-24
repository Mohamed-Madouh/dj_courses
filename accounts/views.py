# from django.contrib.auth import login,authenticate
# from django.http import HttpResponse
# from django.shortcuts import render, redirect ,get_object_or_404
# from .forms import ProfileUpdateForm,SignUpForm
# from .models import profile
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.views import LoginView
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import requires_csrf_token


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from django.contrib import messages
from .forms import SignUpForm, ProfileUpdateForm
from .models import profile
from django.contrib.auth.views import LoginView

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile.objects.create(user=user)  # Create the profile for the user
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('accounts:profile')  # Use 'accounts:profile' to include the app namespace
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = "registration/login.html"  # Customize this template as needed

@requires_csrf_token
@login_required
def Profile(request):
    profile_instance = get_object_or_404(profile, user=request.user)
    return render(request, 'registration/profile.html', {'profile': profile_instance})

@login_required
def update_profile(request):
    profile_instance = get_object_or_404(profile, user=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile_instance)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=profile_instance)
    return render(request, 'registration/update_profile.html', {'form': form})
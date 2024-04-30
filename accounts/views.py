from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import Signupform,UpdateProfileForm,UpdateUserform,prfileform
from .models import profile,UserPhoneNumber,Social_media


# Create your views here.



def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            eemail = form.cleaned_data.get('email')
            User = Signupform(username=username, password=raw_password,email=eemail)
            User=form.save()
            login(request, User)
            return redirect('home')  # Redirect to the home page after successful signup
    else:
        form = Signupform()
    
    return render(request, 'registration/profile.html', {'form': form})


def profle(request):
    Profile = profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = prfileform(request.POST, request.FILES, instance=Profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = prfileform(instance=Profile)
    return render(request, 'registration/profile.html', {'form': form})


def profilee(request): 
    profilee = profile.objects.get(user = request.user)
    User_Social = Social_media.objects.filter(user=request.user)
    PhoneNumber = UserPhoneNumber.objects.filter(user=request.user)
    return render(request,'registration/profile.html',{'Profile':profilee ,'User_Social':User_Social ,'PhoneNumber':PhoneNumber})
 
     
def profile_edit(request):
  	#Get the profile
    profilee =profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        userform = UpdateUserform(request.POST,instance=request.user)
        profileform = UpdateProfileForm(request.POST,request.FILES,instance=profilee)
        
        if userform.is_valid and profileform.is_valid:
            userform.save()
            new_profile = profileform.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            return redirect('/accounts/profile')
    else:
        userform = UpdateUserform(instance=request.user)
        profileform = UpdateProfileForm(instance=profile)
    
    return render(request ,'accounts/profile_edit.html',context={'form1':userform,'form2':profileform})

def update_user(request):
    user = request.user  # Retrieve the current user instance

    if request.method == 'POST':
        form = UpdateUserform(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Save the updated user information
            return redirect('profile')  # Redirect to the profile page after successful update
    else:
        form = UpdateUserform(instance=user)
    
    return render(request, 'update_user.html', {'form': form})
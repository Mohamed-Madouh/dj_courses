from django.contrib.auth import login,authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import  UpdateProfileForm,UpdateUserform,SignUpForm
from .models import profile
from django.contrib.auth.forms import AuthenticationForm




# Create your views here.



# def signup(request):
#     if request.method == 'POST':
#         form = Signupform(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             eemail = form.cleaned_data.get('email')
#             User = Signupform(username=username, password=raw_password,email=eemail)
#             User=form.save()
#             login(request, User)
#             return redirect('home')  # Redirect to the home page after successful signup
#     else:
#         form = Signupform()
    
#     return render(request, 'registration/signup.html', {'form': form})


# def profle(request):
#     Profile = profile.objects.get(user=request.user)
#     if request.method == 'POST':
#         form = prfileform(request.POST, request.FILES, instance=Profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = prfileform(instance=Profile)
#     return render(request, 'registration/profile.html', {'form': form})


# def profilee(request): 
#     profilee = profile.objects.get(user = request.user)
#     User_Social = Social_media.objects.filter(user=request.user)
#     PhoneNumber = UserPhoneNumber.objects.filter(user=request.user)
#     return render(request,'registration/profile.html',{'Profile':profilee ,'User_Social':User_Social ,'PhoneNumber':PhoneNumber})
 





# views.py
def login_signup(request):
    if request.method == 'POST':
        if login_form in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')  # Redirect to the home page after login
        elif signup_form in request.POST:
            signup_form = SignUpForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                return redirect('home')  # Redirect to the home page after signup
    else:
        login_form = AuthenticationForm()
        signup_form = SignUpForm()
    
    return render(request, 'login_signup.html', {'login_form': login_form, 'signup_form': signup_form})




# @csrf_exempt
# def login_signup(request):
#     if request.method == 'POST':
#         if  in request.POST:
#             login_form = LoginForm(request.POST)
#             if login_form.is_valid():
#                 username = login_form.cleaned_data['username']
#                 password = login_form.cleaned_data['password']
#                 user = authenticate(request, username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     return render(request, 'login_signup.html')
#         elif registration_form in request.POST:
#             registration_form = RegistrationForm(request.POST)
#             if registration_form.is_valid():
#                 user = registration_form.save()
#                 login(request, user)
#                 return render(request, 'login_signup.html')
#     else:
#         login_form = LoginForm()
#         registration_form = RegistrationForm()

#     return render(request, 'login_signup.html', {'login_form': login_form, 'registration_form': registration_form})



# def login_signup(request):
#     if request.method == 'POST':
#         auth_form = AuthenticationForm(data=request.POST)
#         reg_form = RegistrationForm(data=request.POST)

#         if auth_form.is_valid() and reg_form.is_valid():
#             auth_form.save()
#             return HttpResponse("Registration successful.")
#         else:
#             return HttpResponse("Invalid registration details.")

#     else:
#         auth_form = AuthenticationForm()
#         reg_form = RegistrationForm()

#     return render(request, 'registration/login_signup.html', {'auth_form': auth_form, 'reg_form': reg_form})







     
def profile_edit(request):
  	#Get the profile
    Profile =profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        userform = UpdateUserform(request.POST,instance=request.user)
        profileform = UpdateProfileForm(request.POST,request.FILES,instance=Profile)
        
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
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile





class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image','department','facebook','githup','x','linkedin','number','emil','Address','DateOfBirth']

















class UpdateUserform(forms.ModelForm):
    username=forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={'calss':'form-control'}))
    email=forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username', 'email']
class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField (widget=forms.FileInput(attrs={'class':'form-comtrol-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'from-control','roes':5}))
    dateofbirthday=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    class Meta:
        model = profile
        fields = ['avatar','bio','dateofbirthday']
        
class Signupform(UserCreationForm):
    phone =forms.CharField()
    dateofbirthday=forms.DateField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2','phone','dateofbirthday']
        
class prfileform (forms.ModelForm):
    class Mate:
        model = profile
        fields =['image','department','address','dateofbirthday']

     
               
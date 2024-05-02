from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile, UserPhoneNumber, Social_media




class SignupForm(UserCreationForm):
    image = forms.ImageField(label="User Image")
    department = forms.CharField(label="Department", max_length=50)
    address = forms.CharField(label="Address", max_length=50)
    dateofbirthday = forms.DateField(label="Date of Birthday")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'image', 'department', 'address', 'dateofbirthday')


class UserPhoneNumberForm(forms.ModelForm):
    class Meta:
        model = UserPhoneNumber
        fields = ('number', 'type')


class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = Social_media
        fields = ('facebook', 'githup', 'x', 'linkedin', 'emil')
class ProfileForm(forms.ModelForm):
    username = forms.CharField(label="Username")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = profile
        fields = ('image', 'department', 'address')




















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

     
               
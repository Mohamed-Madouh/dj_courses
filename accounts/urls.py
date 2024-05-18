from django.urls import path
from .views import  signup,Profile,update_profile, CustomLoginView
from django.contrib.auth.views import  LoginView 


app_name ='accounts'
urlpatterns = [
    path('signup/', signup, name='signuup'),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('profile/', Profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path("logout/", LoginView.as_view(), name="logout"),

]
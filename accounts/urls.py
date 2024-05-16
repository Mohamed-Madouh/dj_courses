from django.urls import path
from .views import  signup,CustomLoginView,profile
from django.contrib.auth.views import  LogoutView

app_name ='accounts'
urlpatterns = [
     path('signup/', signup, name='signuup'),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('profile/', profile, name='profile'),
    path("logout/", LogoutView.as_view(), name="logout"),

   
   

]
from django.urls import path
from .views import  profile_edit ,update_user,login_signup

app_name ='accounts'
urlpatterns = [
     path('login_signup/', login_signup, name='login_signup'),
    path('profile/update/', update_user, name='update_user'),
    path('profile/edit/', profile_edit, name='profile_edit'),
   
   

]
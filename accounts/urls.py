from django.urls import path
from .views import  profile_edit ,signup ,update_user
from . import views
app_name ='accounts'
urlpatterns = [
    path('signup/',signup,name='signup'),

    path('profile/update/', update_user, name='update_user'),
    path('profile/edit/', profile_edit, name='profile_edit'),
   
   

]
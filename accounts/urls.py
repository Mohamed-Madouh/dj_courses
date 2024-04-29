from django.urls import path
from .views import profilee ,profile_edit ,signup ,update_user
from . import views
app_name ='accounts'
urlpatterns = [
    path('signup/',views.signup ,name='signup'),
    path('profile/',views.profilee,name='profile'),
    path('profile/update/', views.update_user, name='update_user'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
   
   

]
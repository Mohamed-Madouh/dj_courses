from django.urls import path
from .views import profilee ,profile_edit ,signup ,update_user
from . import views
app_name ='accounts'
urlpatterns = [
    path('signup/post',signup,name='signup'),
    # path('profle/',profle,name='profle'),
    path('profle/',profilee,name='profle'),
    path('profile/update/', update_user, name='update_user'),
    path('profile/edit/', profile_edit, name='profile_edit'),
   
   

]
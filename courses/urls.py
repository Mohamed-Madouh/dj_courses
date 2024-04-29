from django.urls import path
from .views import courses_list
app_name ='courses'
urlpatterns = [
    path('home/', courses_list, name='home-page'),
    ]
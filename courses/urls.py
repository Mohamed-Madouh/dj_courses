from django.urls import path
from .views import courses_list,coursesdetail
app_name ='courses'
urlpatterns = [
    path('', courses_list, name='home-page'),
    path('<int:pk>', coursesdetail.as_view(), name = 'courses_detail'),
    ]
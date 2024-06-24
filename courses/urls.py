from django.urls import path
from .views import courses_list,coursesdetail,productlist,courses_detail
from . import views
app_name ='courses'
urlpatterns = [
    
    path('', courses_list, name='home-page'),
    path('<int:id>/', views.courses_detail, name='course_detail'),    
    ]


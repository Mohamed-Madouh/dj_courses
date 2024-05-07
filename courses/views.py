from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView ,DetailView
from .models import Section , courses
# Create your views here.
class productlist(ListView):
    model = courses
class coursesdetail(DetailView):
    model = courses
    
def courses_list(request):
    sections = Section.objects.all()
    return render(request, 'courses/courses_list..html', {'sections': sections})




def courses_detail(request, id):
    courses_detail =courses.objects.get(id=id) 
    return render(request, 'courses/course_detail.html', {'course': courses_detail})
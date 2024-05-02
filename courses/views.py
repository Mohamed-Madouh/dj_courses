from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from .models import Section , courses
# Create your views here.
class productlist(ListView):
    model = courses
    paginate_by =50
class productdetail(DetailView):
    model = courses
def courses_list(request):
    sections = Section.objects.all()
    return render(request, 'registration/home.html', {'sections': sections})
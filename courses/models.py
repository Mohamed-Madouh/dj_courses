from django.db import models

# Create your models here.
from django.utils.translation import gettext as _ # type: ignore
from django.contrib.auth.models import User # type: ignore
# Create your models here.


class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class courses(models.Model):
    rodmapimage=models.ImageField(_("rodmapimage"), upload_to='rodmap_image')
    section = models.ForeignKey(Section, related_name='courses',verbose_name="section", on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=True)
    image=models.ImageField(_("image"),upload_to='courses_image')
    name=models.CharField(_("name"),max_length=50)
    rate=models.IntegerField(verbose_name="rate")
    doctorname=models.ForeignKey('course_content',verbose_name="doctor_name", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class course_content(models.Model):
    doctorname=models.CharField(_("doctor_name"), max_length=60)
    department=models.CharField(_("Department"), max_length=50)
    subtitelcourse=models.TextField(_("about"),max_length=300)
    subtiteldoc=models.TextField(_("about"),max_length=300)
    vediourl=models.URLField(null=True,blank=True)
    urlcourses=models.URLField(null=True,blank=True)
    image = models.ImageField(_("userimage"),upload_to='doctor_image' , null=True ,blank=True)
    def __str__(self):
        return self.doctorname
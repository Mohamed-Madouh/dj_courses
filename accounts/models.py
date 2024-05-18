from django.db import models # type: ignore
from django.contrib.auth.models import User
from django.utils.translation import gettext as _ 
from django.dispatch import receiver
from django.db.models.signals import post_save

class profile(models.Model):
    user=models.OneToOneField(User, related_name='profile',verbose_name="user_profile", on_delete=models.CASCADE)
    Address = models.CharField(_("Address"), max_length=50, null= True ,blank= True)
    image = models.ImageField(upload_to='users/',verbose_name="user image" ,default="media/profile.png")
    department=models.CharField(_("Department"), max_length=50)
    facebook=models.URLField(_("facebook"), null= True ,blank= True)
    githup=models.URLField(_("githup"), null= True ,blank= True)
    x=models.URLField(_("x"), null= True ,blank= True)
    linkedin=models.URLField(_("linkedin"), null= True ,blank= True)
    emil=models.EmailField(_("emil") , null= True ,blank= True)
    number=models.CharField(_("phone_number"),max_length=11, null= True ,blank= True)
    DateOfBirth= models.DateField(_("Date Of Birth"), null= True ,blank= True)
  

    def __str__(self):
        return str(self.user)
    
    
@receiver(post_save,sender=User)
def create_profile ( sender , instance ,created , **kwargs ):
    if created:
        profile.objects.create(user= instance)




@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
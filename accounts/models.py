from django.db import models # type: ignore
from django.contrib.auth.models import User
from django.utils.translation import gettext as _ 
from django.dispatch import receiver
from django.db.models.signals import post_save

class profile(models.Model):
    user=models.OneToOneField(User, related_name='user_profile',verbose_name="user_profile", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users/',verbose_name="user image")
    department=models.CharField(_("Department"), max_length=50)
    address=models.CharField(_("adress"),max_length=50)

    def __str__(self):
        return str(self.user)
    
    
@receiver(post_save,sender=User)
def create_profile ( sender , instance ,created , **kwargs ):
    if created:
        profile.objects.create(user= instance)



DATE_TYPE = {
    ('Home','Home'),
    ('Office', 'Office' ),
    ('Academy', 'Academy' ),
    ('Other', 'Other' )
}
class UserPhoneNumber(models.Model):
    user=models.ForeignKey(User,related_name='user_phonr',verbose_name="user_phonr", on_delete= models.CASCADE )
    number=models.CharField(_("phone_number"),max_length=11)
    type = models.CharField(_("Type your number"),choices=DATE_TYPE , max_length=10)
   
class Social_media(models.Model):
    user=models.ForeignKey(User,related_name='Social_media_user',verbose_name="Social_media_user",on_delete=models.CASCADE)
    facebook=models.URLField(_("facebook"))
    githup=models.URLField(_("githup"))
    x=models.URLField(_("x"))
    linkedin=models.URLField(_("linkedin"))
    emil=models.EmailField(_("emil"))
  

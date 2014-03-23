from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user=models.OneToOneField(User,related_name='profile')
  
  
  
  def __unicode__(self):
    return self.user.username

  
  
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
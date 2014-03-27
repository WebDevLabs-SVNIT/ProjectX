from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
from django.contrib.auth.models import User,Group,Permission

#Faculties=Group.objects.get_or_create(name='Faculties')
#Students=Group.objects.get_or_create(name='Students')
p=Group.objects.all()
Faculties=p[0]
Students=p[1]


class Branch(models.Model):
  COURSES=(('B.TECH','B.TECH'),('M.SC','M.SC'))
  YEARS=(('1','FIRST'),('2','SECOND'),('3','THIRD'),('4','FOURTH'),('5','FIFTH'))
  name=models.CharField('Branch Name',max_length=50)
  year=models.CharField('year',max_length=1,choices=YEARS)
  division=models.CharField(max_length=1,default='A')
  course=models.CharField('Course',max_length=8,choices=COURSES)
  
  def __unicode__(self):
    return self.name + " " + self.year + " " + self.division  
  
class Subject(models.Model):
  code=models.CharField(max_length=10)
  name=models.CharField(max_length=50)
  
  def __unicode__(self):
    return self.name

class StudentUserProfile(models.Model):
  user=models.OneToOneField(User,related_name='sprofile')
  branch=models.ForeignKey(Branch)
  
  
  def __unicode__(self):
    return self.user.username

User.sprofile = property(lambda u: StudentUserProfile.objects.get_or_create(user=u)[0] if u.groups.filter(name='Faculties').count()==0 else None)


class FacultyUserProfile(models.Model):
  
  user=models.OneToOneField(User,related_name='tprofile')
  subjects=models.ManyToManyField(Subject,related_name='Faculties')  
  
  def __unicode__(self):
    return self.user.username
  
User.fprofile = property(lambda u: FacultyUserProfile.objects.get_or_create(user=u)[0] if u.groups.filter(name='Students').count()==0 else None )


@receiver(post_save,sender=StudentUserProfile)
def my_handler_one(sender, **kwargs):
  if kwargs['created']:
    obj=kwargs['instance']
    u=obj.user
    u.groups.add(Students)
    
    
    

@receiver(post_save,sender=FacultyUserProfile)
def my_handler_two(sender, **kwargs):
	if kwargs['created']:
		obj=kwargs['instance']
		obj.user.groups.add(Faculties)
		obj.save()

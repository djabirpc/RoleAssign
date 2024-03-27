from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.
 
class Role(models.Model):
  name = models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
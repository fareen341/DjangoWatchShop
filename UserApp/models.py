from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

seller,status=Group.objects.get_or_create(name='seller')
customer,status=Group.objects.get_or_create(name='customer')

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    class Meta:
        db_table = 'UserProfiledb'

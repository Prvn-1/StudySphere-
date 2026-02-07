from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=200)
    department = models.CharField(max_length=150, blank=True)
    year = models.IntegerField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', default='profiles/default.jpg', null=True, blank=True)


    def __str__(self):
        return self.user.username


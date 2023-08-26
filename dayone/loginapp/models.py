from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Collection(models.Model):
    image = models.ImageField(default="default.jpg",upload_to='gallery')

class UserCollection(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    imageID = models.ForeignKey(Collection,on_delete=models.CASCADE)
    




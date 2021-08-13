from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Creating 1 to 1 relationship for user profiles

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' 

    def save(self):
        """we are chopping down the size of user profile if in case the image large and takes lof of time
        to load on the browser
        """
        super().save()# saving the image from the class

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :#chopp the image to (300,300) size
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
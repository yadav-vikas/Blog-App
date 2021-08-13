from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Creating 1 to 1 relationship for user profiles

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' 

    def save(self, ** kwargs):
        """we are chopping down the size of user profile if in case the image large and takes lof of time
        to load on the browser

        Note:When you are overriding model's save method in Django, you should also pass *args and **kwargs to overridden method.
        ERROR - u might get an error called ------- save() got an unexpected keyword argument 'force_insert'-------- 
        because in save method by defualt force_insert=True , to overcome this we must pass ** kwargs as well.
        Why ? 
        >>>>>>>every function has a "signature", a pattern of arguments. 
        If you override save with a new definition that doesn't take any arguments (except the implicit self), 
        you get the reported error when it is passed an argument it is expected to handle, e.g. force_insert. 
        The *args, **kwargs syntax says, "collect all positional args in the args list and all keyword args in the kwargs dict".
         Then they can be passed along via the super call to do their work.
        """
        super().save()# saving the image from the class

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :#chopp the image to (300,300) size
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
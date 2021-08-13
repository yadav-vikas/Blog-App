from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User # one to many relationship

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #auto_now_add = True --> time at when post was created
    #auto_now =True --> time at when the post was updated
    #default=timezone.now a function Returns a datetime that represents the current point in time. 
    # NOTE: we are note executing the timezone.now() function for any new values since we want only defualt value

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # on_delete to delete content related to the author
    # NOTE: when a author deleted all posted are deleted related to that author

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        """[redirect vs reverse] : redirect will send you back to some url mentioned
         on the other hand reverse will simply return the full url as string 
         and that string can be handled by views to route the url

        Returns:
            [self]: [description]
        """
        return reverse('post-detail',kwargs={'pk':self.pk})

    
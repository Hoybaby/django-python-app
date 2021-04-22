from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
# a text field is similar to charfield but textfield is unrestricted text where it can have lines after lines with each other
# line 13 on_delete is for if a user gets deleted by  an admin or they delete their own account, the posts they have made will also get deleted.
# why are we using the reverse function instead of redirect?
# redirect will atually redirect for a specifc route and reverse will return the full url to that route as a string. we want the view to handle the redirect sowe use reverse


class Post(models.Model):
    title =  models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
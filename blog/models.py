from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# a text field is similar to charfield but textfield is unrestricted text where it can have lines after lines with each other
# line 13 on_delete is for if a user gets deleted by  an admin or they delete their own account, the posts they have made will also get deleted.

class Post(models.Model):
    title =  models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)





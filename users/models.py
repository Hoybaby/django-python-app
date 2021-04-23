from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

# this on delete i used on user that if the user is delete, the posts and now the PROFILE will be deleted.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # this will make the directory for where the pictures go
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # after this we need to have a dunder str method, anytime we print out a profile, it will just say profile object
    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()

    #     # this will open open the image of the current instance
    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
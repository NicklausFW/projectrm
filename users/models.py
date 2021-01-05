from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# user profile have a one to one relationship with the user
# CASCADE menas if we delete the user then the profile is deleted
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    # save super big image
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        # resize image
        img = Image.open(self.image.path)
        # 300 pixels x 300 pixels
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

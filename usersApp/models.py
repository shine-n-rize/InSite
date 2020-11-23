from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    branch = models.CharField(max_length=200, null=True)
    degree = models.CharField(max_length=5, null=True)
    year_of_joining = models.IntegerField(null=True)
    dob = models.CharField(max_length=10, null=True)
    image = models.ImageField(default='profile_pics/dummy.png', upload_to='profile_pics/', null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('search-profile', kwargs={'pk': self.pk})
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Club(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_clubs():
        return Club.objects.all()


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    post_image = models.ImageField(
        upload_to='postsApp/posts', blank=True, null=True)
    date_posted = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='postsApp/videos',
                             default=None, blank=True, null=True)
    add_to_club = models.ForeignKey(
        Club, on_delete=models.CASCADE, default='Others')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    @staticmethod
    def get_all_posts_by_club_id(club_id):
        if club_id:
            return Post.objects.filter(add_to_club=club_id)
        else:
            return Post.objects.all()

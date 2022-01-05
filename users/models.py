import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from memberships.models import Membership
from video_service import settings
from videos.models import Movie, UserMovie


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    birth_date = models.DateField()
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
    stripe_customer_id = models.CharField(max_length=64)
    movies = models.ManyToManyField(Movie, through=UserMovie, related_name="profiles")

    @property
    def age(self):
        diff = datetime.date.today() - self.birth_date
        return diff.days // 365

    def __str__(self):
        return self.user.username

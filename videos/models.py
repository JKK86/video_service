from django.db import models
from django.utils import timezone

from memberships.models import Membership

PREVIEW = "pre"
PUBLISHED = "pub"

SINGLE = "single"
SERIES = "series"

R_ALL = "rating_system_all.svg"
R_7 = "rating_system_7.svg"
R_12 = "rating_system_12.svg"
R_16 = "rating_system_16.svg"
R_18 = "rating_system_18.svg"


class Genre(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]


class Movie(models.Model):

    STATUS_CHOICES = (
        (PREVIEW, "preview"),
        (PUBLISHED, "published")
    )

    TYPE_CHOICES = (
        (SINGLE, "single"),
        (SERIES, "series")
    )

    AGE_CHOICES = (
        (R_ALL, "All"),
        (R_7, "7"),
        (R_12, "12"),
        (R_16, "16"),
        (R_18, "18")
    )

    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    description = models.TextField()
    genres = models.ManyToManyField(Genre)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PREVIEW)
    allowed_membership = models.ManyToManyField(Membership)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=SINGLE)
    thumbnail = models.ImageField(upload_to="thumbnails", blank=True, null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    age_limit = models.CharField(max_length=24, choices=AGE_CHOICES, default=R_ALL)


class Video(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    description = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="videos")
    file = models.FileField(upload_to="movies")
    order = models.PositiveIntegerField()


class UserMovie(models.Model):
    STARS = (
        (0, "☆☆☆☆☆☆☆☆☆☆"),
        (1, "★☆☆☆☆☆☆☆☆☆"),
        (2, "★★☆☆☆☆☆☆☆☆"),
        (3, "★★★☆☆☆☆☆☆☆"),
        (4, "★★★★☆☆☆☆☆☆"),
        (5, "★★★★★☆☆☆☆☆"),
        (6, "★★★★★★☆☆☆☆"),
        (7, "★★★★★★★☆☆☆"),
        (8, "★★★★★★★★☆☆"),
        (9, "★★★★★★★★★☆"),
        (10, "★★★★★★★★★★"),
    )

    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    is_watched = models.BooleanField(null=True)
    to_watch = models.BooleanField(null=True)
    rating = models.IntegerField(choices=STARS, default=0)

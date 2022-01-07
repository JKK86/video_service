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


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status=PUBLISHED)


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
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PREVIEW)
    allowed_membership = models.ManyToManyField(Membership)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=SINGLE)
    thumbnail = models.ImageField(upload_to="thumbnails", blank=True, null=True)
    age_limit = models.CharField(max_length=24, choices=AGE_CHOICES, default=R_ALL)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title

    @property
    def rating(self):
        movie_ratings = [x.rating for x in self.usermovie_set.all()]
        return round(sum(movie_ratings) / len(movie_ratings))


class Video(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    description = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="videos")
    file = models.FileField(upload_to="movies")
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order}. {self.title}"


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

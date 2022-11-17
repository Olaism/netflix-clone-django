import uuid
from django.db import models


class FeaturedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(featured=True)


class Movie(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    flyer = models.ImageField(upload_to='media/images/')
    release_date = models.DateField()
    duration = models.PositiveIntegerField()
    rating = models.FloatField(null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    seasonal = models.BooleanField(default=False)
    category = models.ManyToManyField('Category', related_name='movies')
    featured = models.BooleanField(default=False)
    objects = models.Manager()
    features = FeaturedManager()

    def __str__(self):
        return f"{self.id} {self.release_date} {self.rating} {self.seasonal}"

    @property
    def is_seasonal(self):
        return self.seasonal


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

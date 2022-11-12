import uuid
from django.db import models

class Movie(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=255)
    flyer = models.ImageField(upload_to='media/images/')
    release_date = models.DateField()
    rating = models.FloatField(null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    seasonal = models.BooleanField(default=False)
    category = models.ManyToManyField('Category', related_name='movies')

    def __str__(self):
        return f"{self.uuid} {self.release_date} {self.rating} {self.seasonal}"

    @property
    def is_seasonal(self):
        return self.seasonal

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

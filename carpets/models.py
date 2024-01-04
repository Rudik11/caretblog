# carpets/models.py
from django.db import models

class CarpetPost(models.Model):
    photo = models.ImageField(upload_to='post_photos/')
    title = models.CharField(max_length=200)
    characteristics = models.TextField()
    description = models.TextField()
    store_link = models.URLField()

    def __str__(self):
        return self.title
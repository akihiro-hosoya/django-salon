from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
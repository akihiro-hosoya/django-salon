from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Salon(models.Model):
    name = models.CharField('店舗', max_length=100)
    address = models.CharField('住所', max_length=100, null=True, blank=True)
    tel = models.CharField('電話番号', max_length=100, null=True, blank=True)
    description = models.TextField('説明', default="", blank=True)
    image = models.ImageField(upload_to='images', verbose_name='店舗外観', null=True, blank=True)

    def __str__(self):
        return self.name
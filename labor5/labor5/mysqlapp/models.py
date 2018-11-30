from django.db import models
from django.urls import reverse

# Create your models here.
class Books(models.Model):
    BookTitle = models.CharField(max_length=100)
    Description = models.TextField(max_length=255)

    def get_absolute_url(self):
        return reverse('main:detail', args=[self.id])

from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name_plural = "Fotos"
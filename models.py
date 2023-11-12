from django.db import models

# Create your models here.
class post(models.Model):
    judul = models.CharField(max_length=20, blank=True)
    body = models.TextField()
    email = models.EmailField(default='azizah@web.com')

    def __str__(self) :
        return "{}. {}", format(self.id.self.judul)
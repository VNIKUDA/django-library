from django.db import models

# Create your models here.
class LibraryBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    avaliable = models.BooleanField()

    def __str__(self):
        return f"{self.author} - {self.title}"
    
    class Meta():
        ordering = ["-avaliable"]

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()

    def __str__(self) -> str:
        return self.title
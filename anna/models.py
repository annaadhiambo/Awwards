from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

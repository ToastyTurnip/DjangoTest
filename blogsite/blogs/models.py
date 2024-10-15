from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 200)
    content = models.CharField(max_length = 10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField("publication date",auto_now = True)

    def __str__(self):
        return self.title

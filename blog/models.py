from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if a user is deleted then the post is deleted

    def __str__(self):
        return self.title 
# after posted has beeen created, for it to be redirected properly
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
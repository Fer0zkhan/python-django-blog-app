from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=200, null=False, blank=False, unique=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False, unique=True)

    bio = models.TextField(null=True, blank=True)
    user_avatar = models.ImageField(null=True,
                                    default="avatar.png")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.username


class Topic(models.Model):
    topic_title = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.topic_title


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)

    blog_title = models.CharField(max_length=100, null=False, blank=False)
    blog_image = models.ImageField(null=False, blank=False)
    blog_description = models.TextField(null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.blog_title

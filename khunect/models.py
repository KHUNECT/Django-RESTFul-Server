from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    userId = models.CharField(max_length=20)
    password = models.PasswordField(max_length=100)
    realname = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phoneNum = models.CharField(max_length=20)
    image = models.ImageField(default='media/default_image.jpeg')

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    context = models.TextField()
    date = models.DateField(default=datetime.now)
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    context = models.TextField()



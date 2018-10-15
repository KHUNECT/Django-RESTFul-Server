from django.db import models
import datetime
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.
class User(models.Model):
    userId = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    realname = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phoneNum = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/original', default='media/default_image.jpeg')

    def save(self):
		#Opening the uploaded image
        im = Image.open(self.image)

        output = BytesIO()

		#Resize/modify the image
        im = im.resize( (300,300) )

		#after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)

		#change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super(User, self).save()
        


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    context = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class ImagePost(Post):
    image1 = models.ImageField(default='')
    image2 = models.ImageField(default='')
    image3 = models.ImageField(default='')

    class Meta:
        abstract = True

class Lecture(models.Model):
    lectureID = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    time = models.CharField(max_length=40)
    professor = models.CharField(max_length=25)

class LecturePost(ImagePost):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

class LectureComment(models.Model):
    post = models.ForeignKey(LecturePost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    context = models.TextField()


    
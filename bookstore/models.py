from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    rating = models.CharField(max_length=2)
    img = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)

# class BooksImages(models.Model):
#     name = models.CharField(max_length=200)
#     book_img = models.ImageField(upload_to='bookstore/static/')

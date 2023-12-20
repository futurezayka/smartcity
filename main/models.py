from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title

from django.db import models
import os


class File(models.Model):
    name = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000, blank=True, null=True)
    file = models.FileField(upload_to="files/")

    def __str__(self):
        return self.name

    def filename(self):
        return os.path.basename(self.file.name)


class Photo(models.Model):
    big_photo = models.ImageField(upload_to="photos/big/")
    small_photo = models.ImageField(upload_to="photos/small/")
    desc = models.CharField(max_length=1000, blank=True, null=True)


class Video(models.Model):
    youtube_id = models.CharField(max_length=50)
    name = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class Counter(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

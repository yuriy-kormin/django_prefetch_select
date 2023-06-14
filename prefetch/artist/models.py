from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=300, null=True, unique=True)


class Tag(models.Model):
    name = models.CharField(max_length=300, null=True, unique=True)


class Artist(models.Model):
    name = models.CharField(max_length=300, null=True, unique=True)
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Group, related_name='artist_list', blank=True)

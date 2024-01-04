from django.db import models

class My(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/photos/', blank=True)
    summary = models.TextField()
class Link(models.Model):
    github = models.URLField(max_length=250, null=True, blank=True)
    linkdenin = models.URLField(max_length=250, null=True, blank=True)
    twitter = models.URLField(max_length=250, null=True, blank=True)
    Facebook = models.URLField(max_length=250, null=True, blank=True)
    instagram = models.URLField(max_length=250, null=True, blank=True)
    cv = models.URLField(max_length=250, null=True, blank=True)


class Skill(models.Model):
    skill = models.CharField(max_length=250)
    


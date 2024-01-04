from django.shortcuts import render
from .models import My, Link, Skill
from PIL import Image
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

def show_my(request):
    my = My.objects.all()
    link = Link.objects.all()
    skill = Skill.objects.all()
    return render (request, 'my/my.html', {'my' : my,
                                           'link' : link,
                                           'skill' : skill})

@receiver(post_save, sender=My)
def resize_photo(sender, instance, **kwargs):
    if instance.image:
        image = Image.open(instance.image)
        image = image.resize((400,400))
        image.save(instance.image.path, quality=2000)
from django.conf import settings
from django.db import models

# Create your models here.
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


def upload_location(instance, filename):
    return "{}/{}".format(instance.pk, filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field",
                              height_field="height_field")
    slug = models.SlugField(unique=True)

    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
        # return "/post/{}".format(self.pk)

    class Meta:
        ordering = ["-pk", "-timestamp", "-updated"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug= new_slug
    qs = Post.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "{}-{}".format(slug,qs.first().pk)
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)

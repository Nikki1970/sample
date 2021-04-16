from django.db import models
from model_utils.models import TimeStampedModel

class Post(TimeStampedModel):
    title = models.CharField(max_length=512)
    slug = models.SlugField(max_length=512)
    body = models.TextField()
    author = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "%s by %s" % (self.title, self.author.username)

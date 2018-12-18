from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    view_time = models.PositiveIntegerField(default=0)
    excerpt = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

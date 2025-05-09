from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_modified = models.DateTimeField(auto_now=True)
    date_time_published = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time_created',]

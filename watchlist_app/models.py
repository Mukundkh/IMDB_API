from django.db import models

#Model for the platform details
class StreamPlatForm(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name
class WatchList(models.Model):
    title = models.CharField(max_length=50)
    story_line = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatForm, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

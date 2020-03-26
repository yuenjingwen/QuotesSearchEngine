from django.db import models


# Create your models here.
class Quote(models.Model):
    id = models.IntegerField(primary_key=True)
    quote = models.TextField()
    author = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    likes = models.IntegerField()
    image = models.TextField()

    def __str__(self):
        return self.quote



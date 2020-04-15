from django.db import models

# Create your models here.


class Joke(models.Model):
    joke_text = models.CharField(max_length=200)
    def __str__(self):
        return self.joke_text
    
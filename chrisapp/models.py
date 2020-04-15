from django.db import models

# Create your models here.


class Joke(models.Model):
    joke_text = models.CharField(max_length=200)
    def __str__(self):
        return self.joke_text

class Punchline(models.Model):
    joke = models.ForeignKey(Joke, on_delete=models.CASCADE)
    punchline_text = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.punchline_text
    
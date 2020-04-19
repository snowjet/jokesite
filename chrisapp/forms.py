from django.forms import ModelForm, Textarea
from .models import  Joke

class JokeForm(ModelForm):
    class Meta:
        model = Joke
        fields = ['joke_text', 'punchline_text']
        widgets = {  'joke_text' : Textarea(attrs={'cols': 80, 'rows': 1}),
                    'punchline_text' : Textarea(attrs={'cols': 80, 'rows': 1})}
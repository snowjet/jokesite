from django.forms import ModelForm
from .models import  Joke

class JokeForm(ModelForm):
    class Meta:
        model = Joke
        fields = ['joke_text', 'punchline_text']
    #joke_text = forms.CharField(label='Your Joke', max_length=200, widget=forms.TextInput(attrs={'size': '50'}))
    #punchline_text = forms.CharField(label='and the punchline', max_length=200, widget=forms.TextInput(attrs={'size': '50'}))
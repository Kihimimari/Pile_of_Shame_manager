from datetime import date

from django.forms import ModelForm, DateField, NumberInput, CharField, Textarea, URLField
from viewer.models import Game


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

    first_release_date = DateField(widget=NumberInput(attrs={'type': 'date'}))
    summary = CharField(widget=Textarea, required=False)
    cover = URLField(empty_value="", required=False)

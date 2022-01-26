from django.forms import ModelForm
from .models import Keycap


class KeycapForm(ModelForm):
    # Meta describes data about the functionality

    class Meta:
        model = Keycap
        fields = ['date', 'profile']

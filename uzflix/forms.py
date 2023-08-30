from django import forms
from .models import Izoh, Baho


class CommentForm(forms.ModelForm):
    class Meta:
        model = Izoh
        fields = ("matn", "user","film")
        


class BahoForm(forms.ModelForm):
    class Meta:
        model = Baho
        fields = ['star']
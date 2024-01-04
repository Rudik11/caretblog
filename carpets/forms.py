# carpets/forms.py
from django import forms
from .models import CarpetPost

class CarpetPostForm(forms.ModelForm):
    class Meta:
        model = CarpetPost
        fields = ['photo', 'title', 'characteristics', 'description', 'store_link']

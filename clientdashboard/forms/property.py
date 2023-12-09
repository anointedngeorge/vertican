from django import forms
from matrixpro.models import PropertyMedia



class PropertyForm(forms.ModelForm):
    
    class Meta:
        model = PropertyMedia
        fields = ['image']
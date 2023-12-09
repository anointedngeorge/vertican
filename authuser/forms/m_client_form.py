from django import forms
from django.db.models.query_utils import Q
from django.contrib.auth.forms import UserCreationForm
from authuser.models import User
from django.forms.fields import MultipleChoiceField

# 
from clients.models.m_client import ClientClass
from authuser.models.user_model import User


class ClientModelForm(forms.ModelForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = ClientClass
        fields = "__all__"
        # exclude = ['groups']
    def __init__(self, *args, **kwargs):
        super(ClientModelForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = User.objects.filter(Q(roles_name = 'client'))







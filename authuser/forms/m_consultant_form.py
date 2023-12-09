from django import forms
from django.db.models.query_utils import Q
from django.contrib.auth.forms import UserCreationForm
from authuser.models import User
from django.forms.fields import MultipleChoiceField

# 
from consultants.models.m_consultants import ConsultantClass
from authuser.models.user_model import User


class ConsultantModelForm(forms.ModelForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = ConsultantClass
        fields = "__all__"
        # exclude = ['groups']
    def __init__(self, *args, **kwargs):
        super(ConsultantModelForm, self).__init__(*args, **kwargs)
        self.fields['consultant'].queryset = User.objects.filter(Q(roles_name = 'consultant'))







from django import forms
from django.http import HttpResponse
from django.db.models.query_utils import Q
from django.contrib.auth.forms import UserCreationForm
from authuser.models import User
from django.forms.fields import MultipleChoiceField



class userRegistrationForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['is_active','is_staff','username','email']
        # exclude = ['groups']
    def __init__(self, *args, **kwargs):
        super(userRegistrationForm, self).__init__(*args, **kwargs)


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2 
        
    def save(self, commit=True):
        try:
            user = super(userRegistrationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.is_staff = True
                user.is_active = True
                user.save()
            return user
        except Exception as e:
            return HttpResponse(e)





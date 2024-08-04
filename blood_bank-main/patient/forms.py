from django import forms
from django.contrib.auth.models import User
from . import models
import re

class PatientUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match("^[A-Za-z]+$", username):
            raise forms.ValidationError("Username must contain only alphabets.")
        return username
    
class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = ['age', 'bloodgroup', 'disease', 'address', 'doctorname', 'mobile', 'profile_pic']

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")
        return mobile
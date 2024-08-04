from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . import models
import re

class DonorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match("^[A-Za-z]+$", username):
            raise forms.ValidationError("Username must contain only alphabets.")
        return username
    
class DonorForm(forms.ModelForm):
    class Meta:
        model=models.Donor
        fields=['bloodgroup','address','mobile','profile_pic']
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if len(mobile) != 10 or not mobile.isdigit():
            raise ValidationError("Mobile number must be exactly 10 digits.")
        return mobile    

class DonationForm(forms.ModelForm):
    class Meta:
        model=models.BloodDonate
        fields=['age','bloodgroup','disease','unit']
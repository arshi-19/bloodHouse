from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/Donor/', null=True, blank=True)
    bloodgroup = models.CharField(max_length=10)
    address = models.CharField(max_length=40)
    
    # Adding the RegexValidator for mobile number
    mobile_regex = RegexValidator(regex=r'^\d{10}$', message="Mobile number must be exactly 10 digits.")
    mobile = models.CharField(validators=[mobile_regex], max_length=10, null=False)
   
    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
    
    @property
    def get_instance(self):
        return self
    
    def __str__(self):
        return self.user.first_name

class BloodDonate(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    disease = models.CharField(max_length=100, default="Nothing")
    age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.donor

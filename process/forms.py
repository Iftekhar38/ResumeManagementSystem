from django import forms
from process.models import *
import random
# from process.utils import sendTextMessage
from django.conf import settings 
from django.core.mail import send_mail

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    def clean_otp(self):
        email =  self.cleaned_data['email']
        # otp = self.cleaned_data['otp']
        otp = random.randint(100000,999999)
        touser = email
        sub = 'OTP'
        body = 'Welcome to RMS and Your OTP is' + str(otp)
        efrom = settings.EMAIL_HOST_USER
        reclist = [touser]
        send_mail(sub, body, efrom,reclist)
        
       # message = 'Welcome to RMS and Your OTP is' + str(otp)
        #sendTextMessage(message, cno)
        return otp
    
    class Meta:
        model = RegistrationModel
        exclude = ('status',)
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm 
from .models import BinanceUser 
 
class BinanceUserCreationForm(UserCreationForm):    
    class Meta:        
        model = BinanceUser        
        fields = ('email', )  
class BinanceUserChangeForm(UserChangeForm):    
    class Meta:        
        model = BinanceUser       
        fields = UserChangeForm.Meta.fields
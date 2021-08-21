from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import BinanceUserChangeForm, BinanceUserCreationForm
from .models import BinanceUser

class BinanceUserAdmin(UserAdmin):    
    add_form = BinanceUserCreationForm
    form = BinanceUserChangeForm
    model = BinanceUser
    list_display = ['email']
admin.site.register(BinanceUser, BinanceUserAdmin)
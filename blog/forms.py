from .models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

# class CustomUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'name', 'email', 'bio', 'user_avatar']

from django.contrib.auth.models import User;
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm;

class RegisterForm(UserCreationForm) :
    class Meta :
        model = User
        fields = ['username', 'email']


class LoginForm(AuthenticationForm) :
    class Meta :
        model = User
        fields = "__all__"

class ChangeUserForm(UserChangeForm) :
    password = None;
    class Meta :
        model = User;
        fields = ['username', 'first_name', 'last_name', 'email']
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm;
from django.contrib.auth import logout;
from django.views.generic import CreateView, TemplateView;
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages

class RegisterView(CreateView) :
    form_class = RegisterForm;
    success_url = reverse_lazy("loginPage")
    template_name = 'register.html'


class LoginPageView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm;

    def get_success_url(self):
        return reverse_lazy("homePage")

    def form_valid(self, form):
        messages.success(self.request, 'Log in successful')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Login credentials incorrect.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login'
        return context
    
class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get(self, request):
        if request.user.is_authenticated:
            return super().get(request)
        else:
            return reverse_lazy('loginPage')
    
def userlogout(request) :
    logout(request);
    return redirect('loginPage')
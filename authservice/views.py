from django.shortcuts import redirect, render;
from .forms import RegisterForm, LoginForm, ChangeUserForm;
from django.contrib.auth import logout;
from django.views.generic import CreateView, TemplateView, UpdateView;
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from order.models import OrderModel;

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
        

def ProfileView(request) :
    orders = OrderModel.objects.filter(user=request.user)
    if request.method == 'POST' :
        profile_form = ChangeUserForm(request.POST, instance=request.user);
        if profile_form.is_valid() :
            profile_form.save();
            messages.success(request, 'Profile Updated Successfully');
            return redirect('profilePage');
    else :
        profile_form = ChangeUserForm(instance=request.user);
    return render(request, 'profile.html', {'form' : profile_form, 'orders': orders})

    
def userlogout(request) :
    logout(request);
    return redirect('loginPage')
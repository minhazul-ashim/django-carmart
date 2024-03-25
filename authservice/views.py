from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm;
from django.contrib.auth import login, authenticate, logout;

# Create your views here.
def register(request) :
    if request.method == 'POST' :
        form = RegisterForm(request.POST);
        if(form.is_valid()) :
            form.save();
            print(form.cleaned_data)
    else :
        form = RegisterForm();
    return render(request, 'register.html', {'form': form});

def userLogin(request) :
    form = LoginForm
    if request.method == 'POST' :
        form = LoginForm(request = request, data = request.POST);
        if(form.is_valid()) :
            name = form.cleaned_data['username'];
            password = form.cleaned_data['password'];
            user = authenticate(username=name, password=password);
            if user is not None :
                login(request, user);
                return redirect('profilePage');
    else :
        form = LoginForm();
        return render(request, 'login.html', {'form' : form});
    return render(request, 'login.html', {'form' : form});


def profile(request) :
    if request.user.is_authenticated :
        return render(request, 'profile.html', {'user' : request.user});
    else :
        return redirect('loginPage')


def userlogout(request) :
    logout(request);
    return redirect('loginPage')
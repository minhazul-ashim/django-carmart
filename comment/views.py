from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView;
from . import forms;

# Create your views here.
class CommentCreateView(CreateView) :
    template_name = '../car/templates/carDetail.html';
    form_class = forms.CommentForm;
    success_url = reverse_lazy("homePage")
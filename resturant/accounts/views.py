from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView

class AccountLogin(LoginView):
    template_name = "login.html"
    next_page =reverse_lazy("menu:homepage")

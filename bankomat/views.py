from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.
class BankAccountsView(ListView):
    model = Card
    template_name = "bankomat.html"
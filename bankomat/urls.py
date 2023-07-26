from django.urls import path
from .views import BankAccountsView

urlpatterns = [
    path("", BankAccountsView.as_view(), name="bankomat"),
]
  
from accounts.views.create import CreateAccount
from .views import CreateAccount, retrive_current_account_details, ListAccounts
from rest_framework.urls import path


urlpatterns = [
    path("list", ListAccounts.as_view(), name="account-list"),
    path("current", retrive_current_account_details, name="current-account-details"),
    path("register", CreateAccount.as_view(), name="account-create")
]
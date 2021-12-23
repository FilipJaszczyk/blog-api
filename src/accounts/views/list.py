from accounts.serializers.list import AccountListSerializer
from accounts.models import Account
from rest_framework import generics

class ListAccounts(generics.ListAPIView):
    queryset = Account.objects.filter(is_active=True)
    serializer_class = AccountListSerializer
from src.accounts.models import Account
from rest_framework import serializers


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "email",
            "given_name",
            "family_name",
        ]

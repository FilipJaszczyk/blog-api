from accounts.models import Account
from rest_framework import serializers


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "email",
            "given_name",
            "family_name",
            "created_at",
            "updated_at",
        ]

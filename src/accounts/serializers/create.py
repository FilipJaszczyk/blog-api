from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from typing import Any
from accounts.models import Account


class AccountCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    given_name = serializers.CharField(max_length=256)
    family_name = serializers.CharField(max_length=256)
    password = serializers.CharField(min_length=8, max_length=64, write_only=True)
    repeated_password = serializers.CharField(
        min_length=8, max_length=64, write_only=True
    )

    def validate(self, attrs) -> Any:
        if attrs["password"] != attrs["repeated_password"]:
            raise ValidationError(detail="Passwords don't match")
        return super().validate(attrs)

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create(
            email=validated_data["email"],
            given_name=validated_data["given_name"],
            family_name=validated_data["family_name"],
            password=validated_data["password"],
        )

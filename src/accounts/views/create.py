from rest_framework import status
from rest_framework.response import Response
from accounts.serializers import AccountCreateSerializer
from rest_framework.generics import CreateAPIView
from drf_spectacular.utils import OpenApiResponse, extend_schema
from drf_spectacular.types import OpenApiTypes


class CreateAccount(CreateAPIView):
    serializer_class = AccountCreateSerializer

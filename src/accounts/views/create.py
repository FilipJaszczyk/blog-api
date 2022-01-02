from rest_framework import status
from rest_framework.response import Response
from accounts.serializers import AccountCreateSerializer
from rest_framework.generics import CreateAPIView
from drf_spectacular.utils import OpenApiResponse, extend_schema
from drf_spectacular.types import OpenApiTypes

@extend_schema(responses={
        201: OpenApiResponse(response=OpenApiTypes.NONE)})
class CreateAccount(CreateAPIView):
    serializer_class = AccountCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(None, status=status.HTTP_201_CREATED, headers=headers)
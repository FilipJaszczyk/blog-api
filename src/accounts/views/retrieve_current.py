from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import HttpRequest
from django.shortcuts import get_object_or_404
from accounts.serializers import AccountDetailSerializer
from rest_framework.status import HTTP_200_OK
from accounts.models import Account
from drf_spectacular.utils import extend_schema

@extend_schema(responses=AccountDetailSerializer)
@api_view(http_method_names=["GET"])
def retrive_current_account_details(request: HttpRequest) -> Response:
    instance = get_object_or_404(Account.objects.filter(id=request.user.id))
    return Response(AccountDetailSerializer(instance=instance).data, status=HTTP_200_OK)
from accounts.models import Account
from accounts.serializers import AccountDetailSerializer
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


@extend_schema(responses=AccountDetailSerializer)
@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
def retrive_current_account_details(request: HttpRequest) -> Response:
    instance = get_object_or_404(Account.objects.filter(id=request.user.id))
    return Response(AccountDetailSerializer(instance=instance).data, status=HTTP_200_OK)

from rest_framework.decorators import detail_route, list_route, parser_classes
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Admin
from rest_framework import viewsets
from django.shortcuts import render, render_to_response, redirect, get_object_or_404


class TokenViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Token.objects.all()
    permission_classes = (AllowAny,)

    @list_route(methods=['post'], url_path='get-token')
    def get_admin_token(self, request, *args, **kwargs):
        req_data = request.data
        rfid = req_data['rfid']
        admin = get_object_or_404(Admin, RFID=rfid)
        token, created = Token.objects.get_or_create(user=admin.user)
        return Response({'token': token.key})
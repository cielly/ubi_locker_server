from rest_framework import viewsets
from .models import Person, Admin, Locker, Access
from .serializers import UserSerializer, PersonSerializer, AdminSerializer, LockerSerializer, AccessSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import detail_route, list_route, parser_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth.models import User
import datetime
from pytz import timezone   

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @detail_route(methods=['post'], url_path='set-rfid')
    def set_RFID(self, request, **kwargs):
    	person = self.get_object()
    	req_data = request.GET
    	rfid = req_data.get('rfid',"0")  #rfid = self.kwargs['rfid'] -> if rfid' was passed as argument
    	setattr(person, 'RFID', rfid)
    	person.save()
    	content = {'message':'RFID updated.'}
    	return Response(content, status=status.HTTP_200_OK)

    @list_route(methods=['post'], url_path='set-rfid')
    @parser_classes((JSONParser,))
    def set_RFID_by_locker_pass(self, request, **kwargs):
        """
        Set RFID of non-admin user. Params: locker_pass; matriculation
        ---
        """
    	req_data = request.data
    	locker_pass = req_data['locker_pass']
    	matriculation = req_data['matriculation']
    	rfid = req_data['rfid']  
    	person = get_object_or_404(Person, matriculation=matriculation)
	if person.locker_password == locker_pass:
		setattr(person, 'RFID', rfid)
	 	person.save()
		content = {'message':'RFID updated.'}
		return Response(content, status=status.HTTP_200_OK)		
	else:
		return Response("Incorrect locker_pass", status=status.HTTP_400_BAD_REQUEST)


class AdminViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LockerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AccessViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Access.objects.all()
    serializer_class = AccessSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    @list_route(methods=['get'], url_path='get-by-rfid')
    @parser_classes((JSONParser,))
    def get_access_by_RFID(self, request, **kwargs):
        req_data = request.GET
        rfid = req_data['rfid']
        locker_id = req_data['locker_id']   
        person = get_object_or_404(Person, RFID=rfid)
        accesses = Access.objects.filter(person_id=person.matriculation)
        recife = timezone('America/Recife')
        current_time = datetime.datetime.now(recife).time()
        for access in accesses:
            if current_time >= access.initial_time and current_time <= access.final_time and locker_id == access.locker.locker_id:
                content = {'access':1, 'message':'access granted.'}
                return Response(content, status=status.HTTP_200_OK)     
        content = {'access':0, 'message':'access denied.'}
        return Response(content, status=status.HTTP_200_OK)

    @list_route(methods=['get'], url_path='get-by-pass')
    @parser_classes((JSONParser,))
    def get_access_by_Locker_Password(self, request, **kwargs):
        req_data = request.GET
        locker_pass = req_data['locker_pass']
        matr = req_data['matriculation']
        locker_id = req_data['locker_id']   
        person = get_object_or_404(Person, matriculation=matr)
        if person.locker_password == locker_pass:
            accesses = Access.objects.filter(person_id=person.matriculation)
            recife = timezone('America/Recife')
            current_time = datetime.datetime.now(recife).time()
            for access in accesses:
                if current_time >= access.initial_time and current_time <= access.final_time and locker_id == access.locker.locker_id:
                    content = {'access':1, 'message':'access granted.'}
                    return Response(content, status=status.HTTP_200_OK)     
        content = {'access':0, 'message':'access denied.'}
        return Response(content, status=status.HTTP_200_OK)



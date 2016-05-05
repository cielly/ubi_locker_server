from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import detail_route
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework import status
from rest_framework.response import Response

class PersonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @detail_route(methods=['post'])
    def set_RFID(self, request, **kwargs):
		person = self.get_object()
		req_data = request.GET
		rfid = req_data.get('rfid',"0")  #rfid = self.kwargs['rfid'] -> if rfid' was passed as argument
		setattr(person, 'RFID', rfid)
		person.save()
		content = {'message':'RFID updated.'}
		return Response(content, status=status.HTTP_200_OK)
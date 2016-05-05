from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import detail_route

class PersonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (AllowAny,)

 #   @detail_route(methods=['post'])
 #   def set_locker_pass(self, request,)

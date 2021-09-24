from rest_framework import viewsets
from .serializers import *


class APIUser(viewsets.ModelViewSet):
    serializer_class = SerialUser  # serializer_class
    queryset = get_user_model().objects.all()


class APIDocumentType(viewsets.ModelViewSet):
    serializer_class = SerialDocumentType
    queryset = DocumentType.objects.all()


class APIProfile(viewsets.ModelViewSet):
    serializer_class = SerialProfile
    queryset = Profile.objects.all()


class APICountry(viewsets.ModelViewSet):
    serializer_class = SerialCountry
    queryset = Country.objects.all()


class APIState(viewsets.ModelViewSet):
    serializer_class = SerialState
    queryset = State.objects.all()


class APICity(viewsets.ModelViewSet):
    serializer_class = SerialCity
    queryset = City.objects.all()


class APIAddress(viewsets.ModelViewSet):
    serializer_class = SerialAddress
    queryset = Address.objects.all()

import logging

from django.core.mail.backends import console
from rest_framework import viewsets, generics, status
from rest_framework.generics import get_object_or_404, RetrieveUpdateAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from clientes.models import Cliente
from clientes.serializer import ClienteSerializer

#@authentication_classes([JWTAuthentication])
#@permission_classes([IsAuthenticated]) #Libera a api para ser autenticada
#@permission_classes([AllowAny]) # libera a api de autenticação


@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
class ClientesView(generics.ListAPIView):
    """Listando todos os clientes."""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
class ClienteCreateView(CreateModelMixin, RetrieveUpdateDestroyAPIView):
    """Detalhes, atualização e criação de um cliente."""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def create(self, request, *args, **kwargs):
        # Lógica personalizada para criar um novo cliente
        return super().create(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Lógica personalizada para manipulação do POST
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # Lógica personalizada antes de salvar o novo objeto
        serializer.save()


@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny]) # libera a api de autenticação
class ClienteUpaDateView(RetrieveUpdateDestroyAPIView):
    """Atualização de um cliente"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def put(self, request, *args, **kwargs):
        # Lógica personalizada para manipulação do PUT
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # Lógica personalizada para manipulação do PATCH
        return super().patch(request, *args, **kwargs)

@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny]) # libera a api de autenticação
class ClienteDeleteView(RetrieveUpdateDestroyAPIView):
    """Deleta um cliente"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def delete(self, request, *args, **kwargs):
        # Lógica personalizada para manipulação do DELETE
        return super().delete(request, *args, **kwargs)




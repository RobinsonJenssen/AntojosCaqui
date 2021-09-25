from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from Productos.models import *  # Se puede borrar porque ya se importa con: from Productos.serializers import *
from Productos.serializers import *


class TipoAPI (viewsets.ModelViewSet):
    serializer_class = TipoSerial
    # queryset => especificamos los objetos que queremos 'comunicar' con el frontend
    queryset = TipoDetalle.objects.all()


class ProductoAPI (viewsets.ModelViewSet):
    serializer_class = ProductoSerial
    queryset = Producto.objects.all()


class ComentarioAPI(viewsets.ViewSet):
    # Permite especificar la lógica de los registros CRUD
    def list(self, request):    # GET
        comentarios = Comentario.objects.all()
        serializador = ComentarioSerial(comentarios, many=True)
        return Response(serializador.data)
    
    def create(self, request):  # POST
        # request => {"usuario": "nomUsuario", "producto": 5}
        serializador = ComentarioSerial(data=request.data)
        # ¿El comentario que se creará cumple los requisitos para alamcaenar en la tabla SQL?
        if serializador.is_valid():
            serializador.save()
            return Response({"Éxito": True})
        return Response(serializador.errors, HTTP_400_BAD_REQUEST)

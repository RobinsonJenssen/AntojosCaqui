from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from .serializer import *


class ShoppingCartAPI(viewsets.ViewSet):
    def list(self, request):
        carts = ShoppingCart.objects.all()
        serializer = CartSerial(carts, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CartSerial(data=request.data)
        if serializer.is_valid():
            cart = serializer.save()
            return Response({"idCart":cart.id})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        cart= get_object_or_404(ShoppingCart, pk=pk)
        data= {"paid", True}
        serializer = CartSerial(cart, data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"update":True})
        return Response(serializer.error, HTTP_400_BAD_REQUEST)


class ArticleAPI(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerial(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerial(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Creates":True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

class InfoShipAPI(viewsets.ViewSet):

    def create(self,request):
        serializer= ArticleSerial(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Creates":True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    def partial_update (self, request, pk=None):
        info= get_object_or_404(InfoShip, pk=pk)
        serializer = CartSerial(info, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response ({"update":True})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
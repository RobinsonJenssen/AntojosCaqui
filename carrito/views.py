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


class ArticleAPI(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerial(articles, many=True)
        return Response(serializer.data)

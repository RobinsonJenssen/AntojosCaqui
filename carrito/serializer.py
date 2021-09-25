from rest_framework import serializers

from .models import *


class CartSerial(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = "__all__"


class ArticleSerial(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class InfoSerial(serializers.ModelSerializer):
    class Meta:
        model = InfoShip
        fields = "__all__"

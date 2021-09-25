from rest_framework import serializers
from .models import *


class SerialUser(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }


class SerialDocumentType(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class SerialProfile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class SerialCountry(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class SerialState(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class SerialCity(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class SerialAddress(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

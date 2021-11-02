from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import UserList, Address


class AddressListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['id', 'country', 'city', 'zip_code',
                  'street', 'house_num', 'apartaments']

    # def create(self, validated_data):
    #     print(validated_data)
    #     result = Address.objects.create(**validated_data)
    #     print('\n'*3, result.id, '\n'*3)
    #     return result

    # def update(self, instance, validated_data):
    #     instance.country = validated_data.get('country', instance.country)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.zip_code = validated_data.get('zip_code', instance.zip_code)
    #     instance.street = validated_data.get('street', instance.street)
    #     instance.house_num = validated_data.get(
    #         'house_num', instance.house_num)
    #     instance.apartaments = validated_data.get(
    #         'apartaments', instance.apartaments)
    #     instance.save()
    #     print('\n'*3, instance, '\n'*3)
    #     return instance


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserList
        fields = ['id', 'username', 'email', 'address']

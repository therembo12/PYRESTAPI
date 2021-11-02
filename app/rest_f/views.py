from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

from .models import Address, UserList
from .serializer import UserListSerializer, AddressListSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserList.objects.all().order_by('id')
    serializer_class = UserListSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressListSerializer


class Address_view:
    class AddressList(APIView):
        def get_all(self, request, format=None):
            address = Address.objects.all()
            serializer = AddressListSerializer(address, many=True)
            return Response(serializer.data)

        def post(self, request, format=None):
            serializer = AddressListSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_BAD)

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from . import serializers
# Create your views here.


class HelloAPIView(APIView):
    """ Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView Feature."""

        an_apiview = [
            'Uses Http methods function (get, post, put, delete, patch)'
            ''
        ]
        return Response({'messing': "Hello!", 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name."""

        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object."""

        return  Response({"method": 'put'})

    def patch(self, request):
        """Patch rquest, only updates fields provides in the request"""

        return Response({'method': 'patch'})

    def delete(self, request):
        """Remove a value of object"""

        return Response({'method': 'patch'})


class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""

    def list(self, request):
        """return a hello message"""

        a_viewset = [
            'Uses actions(list, create, retrieve, update, patial_update, destroy)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',

        ]

        return Response({'message': 'Hello!', 'aviewset':a_viewset})

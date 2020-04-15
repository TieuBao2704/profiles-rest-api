from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions
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


    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """return a hello message"""

        a_viewset = [
            'Uses actions(list, create, retrieve, update, patial_update, destroy)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',

        ]

        return Response({'message': 'Hello!', 'aviewset':a_viewset})

    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HelloSerializer(data= request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        """Handles getting an object by Its ID."""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handles updating an object."""

        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles Remove an object."""

        return Response({'http_method':'DELETE'})


class UserProfilesViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.UserProfilesSerializer
    queryset = models.UserProfiles.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use ObtainAuthToken APIview to validate and create a token"""

        return ObtainAuthToken().post(request)


class UserProfilesFeedViewset(viewsets.ModelViewSet):
    """Handles creating, reading, updating profiles feed item."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemViewSet
    queryset = models.ProfileFeedItems.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

    def perform_feed(self, serializers):
        serializers.save(user_profile = self.request.user)

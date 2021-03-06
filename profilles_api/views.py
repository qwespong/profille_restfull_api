from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profilles_api import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings  
from rest_framework.permissions import IsAuthenticated

from profilles_api import models
from .serializers import ProfileFeedItemSerializer, UserProfileSerializer
from .models import UserProfile
from profilles_api import permissions

# class HelloApiView(APIView):
#     """Test API View"""
#     serializer_class = serializers.HelloSerializer

#     def get(self, request, format=None):
#         """Return list of APIView features"""
#         an_apiview = [
#             'Uses HTTP methods as function(get,post,patch,put,delete)',
#             'Is similar to django views',
#             'Gives you the most controll over your app logic',
#             'Is mapped manually to URLs'
#         ]

#         return Response({'message': 'hello', 'an_apiview': an_apiview})

#     def post(self, request):
#         """Create a hello message with our name"""
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'Hello {name}'
#             return Response({'message': message})
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#     def put(self, request, pk=None):
#         """Handle Updating an object"""
#         return Response({'method': 'PUT'})

#     def patch(self, request, pk=None):
#         """Handle partial Updating an object"""
#         return Response({'method': 'PATCH'})

#     def delete(self, request, pk=None):
#         """Handle deleting an object"""
#         return Response({'method': 'DELETE'})


# class HelloViewSet(viewsets.ViewSet):
#     """Test API ViewSet"""
#     serializer_class = serializers.HelloSerializer

#     def list(self, request):

#         a_viewlist = [
#             'Uses actions (list,create,retrieve,update,partial update)',
#             'Automatically maps to URLS using Routers'
#             'Provides more functionality with less code'
#         ]

#         return Response({'message': 'Hello', 'a_viewlist': a_viewlist})

#     def create(self, request):
#         """Create a new hello message"""
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'Hello {name}!'
#             return Response({'message': message})
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#     def retrieve(self, request, pk=2):
#         """Handle getting an object by its ID"""
#         return Response({'http_method': 'GET'})

#     def update(self, request, pk=None):
#         """Handle updating an object by its ID"""
#         return Response({'http_method': 'PUT'})

#     def partial_update(self, request, pk=None):
#         """Handle updating part an object by its ID"""
#         return Response({'http_method': 'PATCH'})

#     def destroy(self, request, pk=None):
#         """Handle removing an object by its ID"""
#         return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedItem(viewsets.ModelViewSet):
    'Handles creating,reading,updating user feed items'
    serializer_class = ProfileFeedItemSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = models.ProfileFeedItem.objects.all()
    permission_class = (
        permissions.UpdateOwnFeed,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)


    

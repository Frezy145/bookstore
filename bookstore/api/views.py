from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Book, User
from api.serializers import BookSerializer, BookDetailSerializer, UserSerializer, UserDetailSerializer
from api.serializers import UserSignUpSerialiezer, AdminSignUpSerializer

# Mixin class
class SerializerMixin:
    detail_serializer_class = None
    
    # method to get serializer class
    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None :
            return self.detail_serializer_class
        return super().get_serializer_class()
    
#
class BookViewSet(SerializerMixin, ReadOnlyModelViewSet):
    #set serializer class
    serializer_class = BookSerializer
    detail_serializer_class = BookDetailSerializer
    
    def get_queryset(self):
        return Book.objects.all()
   
#
class UserViewSet(SerializerMixin, ReadOnlyModelViewSet):
    #serializer class
    serializer_class = UserSerializer
    detail_serializer_class = UserDetailSerializer
    
    def get_queryset(self):
        return User.objects.all()
 
class UserSignUpViewSet(ModelViewSet):
    
    serializer_class = UserSignUpSerialiezer
    
    def get_queryset(self):
        return User.objects.all()

class AdminSignUpViewSet(ModelViewSet):
    
    serializer_class = AdminSignUpSerializer
    
    def get_queryset(self):
        return User.objects.all()
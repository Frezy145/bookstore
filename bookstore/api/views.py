from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Book, User
from api.serializers import BookSerializer, BookDetailSerializer, UserSerializer, UserDetailSerializer
from api.serializers import UserSignUpSerialiezer

# Mixin class 00
class SerializerMixin:
    detail_serializer_class = None
    
    # method to get serializer class
    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None :
            return self.detail_serializer_class
        return super().get_serializer_class()
    
# 01
class BookViewSet(SerializerMixin, ReadOnlyModelViewSet):
    #set serializer class
    serializer_class = BookSerializer
    detail_serializer_class = BookDetailSerializer
    
    def get_queryset(self):
        return Book.objects.all()
   
# 02
class UserViewSet(SerializerMixin, ReadOnlyModelViewSet):
    #serializer class
    serializer_class = UserSerializer
    detail_serializer_class = UserDetailSerializer
    
    def get_queryset(self):
        if request.user.age < 18:
            return User.objects.filter(access='All')
        return User.objects.all()
 # 03
class UserSignUpViewSet(ModelViewSet):
    
    serializer_class = UserSignUpSerialiezer
    
    def get_queryset(self):
        return User.objects.all()
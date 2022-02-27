from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer
from api.models import Book, User

# Book list serializer
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'autors', 'page']
      
# User list serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

# Book detail serializer
class BookDetailSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'autors', 'page', 'summary', 'created_at']

# User detail serializer
class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'

# User create serializer

class UserSignUpSerialiezer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'gender', 'username', 'email', 'password', 'profile_image' ]

class AdminSignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
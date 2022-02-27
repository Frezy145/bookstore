from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer
from api.models import Book, User

# Book list serializer 1
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'autors', 'number_of_pages']
      
# User list serializer 2
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

# Book detail serializer 3
class BookDetailSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'autors', 'number_of_pages', 'summary', 'created_at']

# User detail serializer 4
class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'

# User create serializer 5

class UserSignUpSerialiezer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'gender', 'username', 'email', 'password', 'profile_image' ]

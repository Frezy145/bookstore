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
        fields = '__all__'
    
    #validate username
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("has already existed")
        return value
    
    # validate password
    def validate(self, data):
        if data['password'] != data['confirmed_password'] :
            raise serializers.ValidationError('Not the same password')
        return data

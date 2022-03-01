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
        fields = ['id','username', 'email', 'age']

# Book detail serializer 3
class BookDetailSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'autors', 'number_of_pages', 'summary', 'created_at']

# Add Book serializer
class AddBookSerializer:
    class Meta:
        model = Book
        fields = '__all__'
    
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
    
    extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            age = validated_data['age'],
            gender = validated_data['gender'],
            username=validated_data['username'],
            email=validated_data['email'],
            profile_image = validated_data['profile_image']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
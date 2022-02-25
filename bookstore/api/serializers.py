from rest_framework.serializers import ModelSerializer
from api.models import Book, Customer

# Book model serializer
class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__ ' # all fields
        
# Customer model serializer
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

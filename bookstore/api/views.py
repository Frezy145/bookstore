from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from api.models import Book, Customer
from api.serializers import BookSerializer, CustomerSerializer
# Mixin class
class SerializerMixin:
    detail_serializer_class = None
    
    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None :
            return self.detail_serializer_class
        return super().get_serializer_class()
    
#
class BookViewSet(SerializerMixin, ReadOnlyModelViewSet):
    #set serializer class
    serializer_class = BookSerializer
    
    def get_queryset(self):
        return Book.objects.all()
    
#
class CustomerViewSet(SerializerMixin, ReadOnlyModelViewSet):
    #serializer class
    serializer_class = CustomerSerializer
    
    def get_queryset(self):
        return Customer.objects.all()

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated

from api.models import Book, User
from api.serializers import BookSerializer, BookDetailSerializer, UserSerializer, UserDetailSerializer
from api.serializers import UserSignUpSerialiezer, AddBookSerializer

# Mixin class 00
class SerializerMixin:
    detail_serializer_class = None
    
    # method to get serializer class
    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None :
            return self.detail_serializer_class
        return super().get_serializer_class()
    
# Book viewset 1
class BookViewSet(SerializerMixin, ReadOnlyModelViewSet):
    #set serializer class
    serializer_class = BookSerializer
    detail_serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.age < 18: # for users under 18 years old
            return Book.objects.filter(access='All')
        return Book.objects.all() 

# Add Book modelviewset 2
class AddBook(SerializerMixin, ModelViewSet):
    
    serializer_class = AddBookSerializer
    detail_serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser] # Only authenticated admin can add books
    
    def get_queryset(self):
        return Book.objects.all()
    
    @action(detail=False, methods=['post'])
    def create_book(self, request):
        data = {}
        serializer = AddBookSerializer (data = request.data)
        serializer.is_valid()
        book = serializer.save()
        data['response'] = 'Successfully added'
        data['title'] = book.name
        data['wallpaper'] = book.image
        return Response(data)
    
    @action(detail=True, methods=['post'])
    def disable(self, request):
        self.get_object().disable() # disable the book
        return Response({'response':'Succesfully disabled'})
        
    @action(detail=True, methods=['post'])
    def enable(self, request):
        self.get_object().enable() # disable the book
        return Response({'response':'Succesfully enabled'})
        
    @action(detail=True, methods=['delete'])
    def delete_book(self, request):
        book = get_object() # get the object
        Book.objects.delete(book) # and delete it 
        return Response ({'response':'Succesfully deleted'})
      
# Book viewset 3
class UserViewSet(SerializerMixin, ReadOnlyModelViewSet):
    
    serializer_class = UserSerializer
    detail_serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser] # Only authenticated admin can see all users
    
    def get_queryset(self):
        return User.objects.all()
    
# Register modelviewset 4
class UserSignUpViewSet(ModelViewSet):
    
    serializer_class = UserSignUpSerialiezer
    
    def get_queryset(self):
        return User.objects.filter(age=100) # that will not return anything
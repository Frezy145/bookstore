from django.contrib import admin
from api.models import User, Book

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    
    list_display = ['profile_image', 'username', 'age', 'gender', 'email']
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    list_display = ['image','name', 'pages', 'autors', 'access', 'active', 'created_at']
    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

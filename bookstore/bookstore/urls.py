"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import BookViewSet, UserViewSet, UserSignUpViewSet, AddBook
from rest_framework.authtoken.views import obtain_auth_token

#set router
router = routers.SimpleRouter()
router.register('books', BookViewSet, basename = 'books')
router.register('users', UserViewSet, basename = 'users')
router.register('register', UserSignUpViewSet, basename = 'signup')
router.register('management', AddBook, basename = 'management')

urlpatterns = [
    path('obtoken/', obtain_auth_token),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include ('rest_framework.urls')),
]

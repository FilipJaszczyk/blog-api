from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework import filters
from .models import Post, User
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    '''
    List all posts, or create new one
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['author__username', 'title']    
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    GET, PUT/PATCH, DELETE
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

class UserRegistration(generics.CreateAPIView):
    '''
    POST method for registering a user
    '''
    serializer_class = UserSerializer


    




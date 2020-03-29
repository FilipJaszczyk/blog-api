from .models import Post, User
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'date_posted', 'date_updated', 'author',] 

'''
USER registration serializer
'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserPostSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    class Meta():
        model = User
        fields = ['id','username', 'posts']

'''
Endpoint 	HTTP Method 	CRUD Method 	Result
'''
# posts 	     GET 	         READ 	      Get all post

# posts/:id     GET 	         READ 	     Get a single post

# posts 	    POST 	        CREATE 	    Add a single puppy

# posst/:id 	PUT 	        UPDATE   	Update a single puppy
        
# puppies/:id 	DELETE 	        DELETE 	    Delete a single puppy
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate

from .views import PostDetail

from .models import Post, User
from .serializers import PostSerializer


class PostListPostDetailTest(APITestCase):
    def setUp(self):
        self.test_user_0 = User.objects.create_user(username='tester', email='tester@email.com', password='tester')

        self.test_user_1= User.objects.create_user(username='tester2', email='tester2@email.com', password='tester2')

        self.test_user_0_post = Post.objects.create(title="First post of user 0", content="POST WAS CREATED", author=self.test_user_0)

        self.test_user_1_post = Post.objects.create(title="POST CREATED 2", content="POST WAS CREATED 2", author=self.test_user_1)

        self.data = {
            'title': 'New title',
            'content':'New content'
        }

    def test_get_posts(self):
        '''
        List of posts GET method test for unauthenticated user
        '''

        response = self.client.get(reverse('posts'))
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Ensure if the data requested is same as one serialized
        self.assertEqual(response.data, serializer.data)
        
    def test_get_detail_post(self):
        '''
        Post detial GET method for unauthenticated user
        '''

        response = self.client.get(reverse('post_detail', kwargs={'pk': self.test_user_1_post.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_object_permission(self):
        '''
        PUT method on another user object
        '''

        self.client.force_authenticate(user=self.test_user_0)
        response = self.client.put(
            reverse('post_detail', kwargs={'pk': self.test_user_1_post.pk}),
            json.dumps(self.data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_object_positive_permission(self):
        '''
        DELETE method on user post 
        '''

        self.client.force_authenticate(user=self.test_user_0)
        response = self.client.delete(reverse('post_detail', kwargs={'pk': self.test_user_0_post.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_token_update_post(self):
        '''
        User is obtaining a token and then updates post 
        '''
        user_data = {
            "username" : "tester",
            "password" : "tester"
        }
        patch_data = {
            "content" : "content changed"
        }
        token_response = self.client.post(reverse('token_obtain_pair'), json.dumps(user_data), content_type='application/json')
        token = token_response.data['access']
        auth_header = "Bearer {}".format(token)

        self.client.credentials(HTTP_AUTHORIZATION= auth_header)
        
        response = self.client.patch(
            reverse('post_detail', kwargs={'pk': self.test_user_0_post.pk}), 
            json.dumps(patch_data), 
            content_type = 'application/json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

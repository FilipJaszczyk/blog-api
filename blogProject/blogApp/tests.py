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

    

# ========= OLD TEST FOR NO AUTHENTICATION ==================
# class PostTestCreateMethod(APITestCase):
#     def test_create_post_unauthenticated(self):
#         '''
#         Ensure we can create new post
#         '''
#         url = reverse('posts')
#         data = {'title': 'Post created', 'content' : 'Post created sucessfully'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class PostTestGetMethod(APITestCase):
#     def setup(self):
#         Post.objects.create(title="POST CREATED", content="POST WAS CREATED")
#         Post.objects.create(title="POST CREATED 2", content="POST WAS CREATED 2")
#         Post.objects.create(title="POST CREATED 3", content="POST WAS CREATED 3")

#     def test_get_posts(self):
#         '''
#         Ensure we can get list of posts
#         '''
#         # get API response 
#         response = self.client.get(reverse('posts'))
#         # get data from DB
#         posts = Post.objects.all()
#         # convert it to JSON
#         serializer = PostSerializer(posts, many=True)
#         # check the status 
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         #check if data is same 
#         self.assertEqual(response.data, serializer.data)
        
# class PostTestPutMethod(APITestCase):
#     def setUp(self):
#         # Posts to be modified 
#         self.first_post = Post.objects.create(title="POST CREATED", content="POST WAS CREATED")
#         self.second_post = Post.objects.create(title="POST CREATED 2", content="POST WAS CREATED 2")
#         #url
#         self.url = 'post_detail'
#         # modifications
#         self.valid_update_post = {
#             "title" : "post is changed",
#             "content": "post is changed"
#         }
#         self.invalid_update_post = {
#             "title": "",
#             "content": "post change"
#         }
#         self.valid_partial_update_post = {
#             "title" : "changed title"
#         }

#         self.invalid_partial_update_post = {
#             "title" : "",
#             "content" : "only content changed"
#         }

#     def test_valid_update_post(self):
#         '''
#         Validated data case for PUT METHOD 
#         '''
#         response = self.client.put(
#             reverse(self.url, kwargs={'pk': self.first_post.pk}),
#             data = json.dumps(self.valid_update_post),
#             content_type = 'application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_invalid_update_post(self):
#         '''
#         Invalid data case PUT METHOD 
#         '''
#         response = self.client.put(
#             reverse(self.url, kwargs={'pk': self.second_post.pk}),
#             data = json.dumps(self.invalid_update_post),
#             content_type = 'application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_valid_partial_update_post(self):
#         '''
#         Valid data case PATCH METHOD 
#         '''
#         response = self.client.patch(
#             reverse(self.url, kwargs={'pk': self.first_post.pk}),
#             data = json.dumps(self.valid_partial_update_post),
#             content_type = 'application/json'
#         )
#         requested_title = self.valid_partial_update_post['title']
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['title'], requested_title)

#     def test_invalid_partial_update_post(self):
#         '''
#         Invalid data case PATCH METHOD 
#         '''
#         response = self.client.patch(
#             reverse(self.url, kwargs={'pk': self.first_post.pk}),
#             data = json.dumps(self.invalid_partial_update_post),
#             content_type = 'application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# class UserTestRegisterMethod(APITestCase):
#     def test_create_valid_user(self):
        url = reverse('register_user')
        data = {
            'username': 'username',
            'email': 'email@email.com',
            'password': 'password'
        }

        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

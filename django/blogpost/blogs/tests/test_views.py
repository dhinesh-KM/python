import json
from rest_framework import status
from ..models import Post,Comment
from  users.models import CustomUser
from ..serializer import PostSerializer,CommentSerializer
from django.test import TestCase,Client
from rest_framework.test import APITestCase
from django.urls import reverse
from bson import ObjectId

client = Client()

class tests(APITestCase,TestCase):
    @classmethod
    def setUpTestData(cls) :
        cls.author1 = CustomUser.objects.create(username = "vimal10", password = '0000',first_name = "vimal", last_name = "nagul", email = '123@gmail.com')
        cls.author1.set_password('0000')
        cls.author1.save()
        cls.author2 = CustomUser.objects.create(username = "arun10", password = '1111',first_name = "arun", last_name = "ganesh", email = '456@gmail.com')
        cls.author3 = CustomUser.objects.create(username = "kumar10", password = '2222',first_name = "dhinesh", last_name = "kumar", email = '789@gmail.com')
        
        
        cls.post = Post.objects.create(title = "django documentation", content = "Everything you need to know about Django.", author = cls.author1)
        cls.post2 = Post.objects.create(title = "mongo documentation", content = "Everything you need to know about mongo.", author = cls.author1)
        
        cls.comment1 = Comment.objects.create(post = cls.post, comment = "Good",user = cls.author1) 
        cls.comment2 = Comment.objects.create(post = cls.post, comment = "Nice",user = cls.author3) 
        
        cls.payload = {'username': 'vimal10', 'password': '0000'}
        response = client.post(reverse('login_user'), data=json.dumps(cls.payload), content_type="application/json")
        #print("o",response.content)
        token = response.data['data']['token']
        cls.token = token


class post_create(tests):
    def setUp(self):
        token = self.token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        #print("**",self.author1)
        self.valid_payload = {
            'title': 'django documentation',
            'content': 'Everything you need to know about Django.',
        }

        self.invalid_payload = { 
                    'title': '',
                    'content': 'Everything you need to know about Django.',
                    }
        
    def test_valid_post(self):
        response = self.client.post(reverse("create-post"), data = json.dumps(self.valid_payload), content_type="application/json")
        #print(response.content.decode())
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        
    def test_invalid_post(self):
        response = self.client.post(reverse("create-post"), data = json.dumps(self.invalid_payload), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        

        
class get_all_post(tests):
    
    def test_all_posts(self):
        response = self.client.get(reverse("get-post"))
        #print(response.content.decode())
        #p = Post.objects.all()
        #serialize = PostSerializer(p,many=True,context={'request': None})
        #self.assertEqual(response.data, {"error":False, "data":serialize.data})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
class get_post(tests):
    def test_valid_post(self):
        response = client.get(reverse('gup-post', kwargs={'pk': self.post.pk}))
        #print(self.post.pk)
        #p = Post.objects.get(pk = ObjectId(self.post.pk))
        #serialize = PostSerializer(p)
        #self.assertEqual(response.data, {'error': False, 'data':serialize.data})
        #print(response.content.decode())
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_invalid_post(self):
        response = client.get(reverse("gup-post", kwargs=  {'pk': '660d2f53eae9ae3a1c39473'}))
        #print(response.content.decode())
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        
class put_post(tests):
    def setUp(self):
        token = self.token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.valid_payload = {'title': 'django documentation','content': 'Everything you need to know about Django.' }
        self.valid_payload1 = {'content': 'Everything you need to know about Django. Parial' }
        self.invalid_payload = {  'title': '', 'content': 'Everything you need to know about Django. Parial'}
        
    def test_put_valid_post(self):
        response = self.client.put(reverse('gup-post', kwargs={'pk': self.post.pk}),
                              data = json.dumps(self.valid_payload), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_patch_valid_post(self): 
        response = self.client.patch(reverse('gup-post', kwargs={'pk': self.post.pk}),
                              data = json.dumps(self.valid_payload1), content_type="application/json")
        #print(response.content.decode())
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_put_invalid_post(self):
        response = self.client.put(reverse('gup-post', kwargs={'pk': self.post.pk}),
                              data = json.dumps(self.invalid_payload), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        
class delete_post(tests):
    def setUp(self):
        token = self.token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
    def test_delete_valid_pos(self):
        response = self.client.delete(reverse('gup-post', kwargs={'pk': self.post.pk}))
        #print(response.content.decode(),response)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        
    
   
class comment_create(tests):
    def setUp(self):
        token = self.token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.post = Post.objects.create(title = "django documentation", content = "Everything you need to know about Django.", author = self.author1)
        #print("author:",self.author1,type(self.author1.pk),"comment:",self.comment1,type(self.comment1.pk),"post:",self.post,type(self.post.pk),self.post,self.post.pk)
        #print("post:",Post.objects.get(pk = self.post.pk))
        post = str(self.post.pk)
        #print(type(self.post.pk))
        self.cvalid_payload = {
            'post_id': post,
            'comment': 'First comment',
        }

        self.cinvalid_payload = { 
                    'post_id': '',
                    'comment': 'Nice comment',
                    }
        
    def test_valid_comment(self):
        #print("//",self.cvalid_payload['post_id'],type(self.cvalid_payload['post_id']))
        response = self.client.post(reverse("create-comment"), data = json.dumps(self.cvalid_payload), content_type="application/json")
        #print("response",response.content,response)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        
    def test_invalid_comment(self):
        response = self.client.post(reverse("create-comment"), data = json.dumps(self.cinvalid_payload), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        
class get_all_comment(tests):
    
    def test_all_comments(self):
        response = client.get(reverse("get-comment"))
        p = Comment.objects.all()
        serialize = CommentSerializer(p,many=True)
        #print(serialize.data, response.data)
        self.assertEqual( response.data,  {'error': False, 'data':serialize.data})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
class get_comment(tests):
        
    def test_valid_comment(self):
        response = client.get(reverse('gup-comment', kwargs={'pk': self.comment1.pk}))
        p = Comment.objects.get(pk = ObjectId(self.comment1.pk))
        serialize = CommentSerializer(p)
        
        self.assertEqual(response.data, {'error': False, 'data':serialize.data})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_invalid_comment(self):
        response = client.get(reverse("gup-comment", kwargs=  {'pk': 'F660d721d2f035b23aaed869e'}))
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        
        
class put_comment(tests):
    def setUp(self):
        token = self.token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        pk = str(self.post.pk)
        self.valid_payload = {'post_id': pk ,'comment': 'first comment' }

        self.valid_payload1 = {  'comment': 'second comment'}
        
        self.invalid_payload = {  'post_id': '', 'comment': '',}
        
    def test_put_valid_comment(self):
        response = self.client.put(reverse('gup-comment', kwargs={'pk': self.comment1.pk}), 
                              data = json.dumps(self.valid_payload), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_patch_valid_comment(self):
        response = self.client.patch(reverse('gup-comment', kwargs={'pk': self.comment1.pk}),
                              data = json.dumps(self.valid_payload1), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_put_invalid_comment(self):
        response = self.client.put(reverse('gup-post', kwargs={'pk': self.comment2.pk}),
                              data = json.dumps(self.invalid_payload), content_type="application/json")
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        
class delete_comment(tests):
    def setUp(self):
        token = self.token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
    def test_delete_valid_comment(self):
        response = self.client.delete(reverse('gup-post', kwargs={'pk': self.post.pk}))
        #print(response.content,response)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 1)
        
        
class get_s_comment(tests):
        
    def test_valid_scomment(self):  
        response = client.get(reverse('get-comment', kwargs={'pk': self.post.pk}))
        #p = Post.objects.get(pk = ObjectId(self.post2.pk))
        #serialize = CommentSerializer(p.comment_set.all(),many = True)
        #print("t",serialize.data,response.data)
        #self.assertEqual(response.data, {'error': False, 'data':serialize.data})
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        


    
from django.test import TestCase
from ..models import Post,Comment
from  users.models import CustomUser
from datetime import datetime

# Create your tests here.
class BlogTest(TestCase):
    
    def setUp(self):
        
        self.author1 = CustomUser.objects.create(username = "vimal10", password = '0000',first_name = "vimal", last_name = "nagul", email = '123@gmail.com')
        self.author2 = CustomUser.objects.create(username = "arun10", password = '1111',first_name = "arun", last_name = "ganesh", email = '456@gmail.com')
        self.author3 = CustomUser.objects.create(username = "kumar10", password = '2222',first_name = "dhinesh", last_name = "kumar", email = '789@gmail.com')
        '''self.blog1 = Blog.objects.create(category = "Django")
        self.blog2 = Blog.objects.create(category = "Python")
        self.blog3 = Blog.objects.create(category = "Web")'''
        
        self.post = Post.objects.create(title = "django documentation", content = "Everything you need to know about Django.",author = self.author1) 
        self.post2 = Post.objects.create(title = "mongo documentation", content = "Everything you need to know about mongo.",author = self.author1) 
        #self.post.blog.set([self.blog1,self.blog2])
        
        self.comment1 = Comment.objects.create(post = self.post, comment = "Good",user = self.author1) 
        self.comment2 = Comment.objects.create(post = self.post, comment = "Nice",user = self.author3) 
        
    '''def test_post_has_blog(self):
        print("*",self.post.blog.all(),self.blog1.category)
        for blog in self.post.blog.all():
            print("Category:", blog.category)
                
        self.assertIn(self.blog1,self.post.blog.all())
        self.assertIn(self.blog2,self.post.blog.all())'''
        
    def test_post_has_title(self):
        self.assertEqual(self.post.title, 'django documentation')
    
    def test_post_has_content(self):
        self.assertEqual(self.post.content, 'Everything you need to know about Django.')
    
    def test_post_has_author(self):
        self.assertEqual(self.post.author, self.author1)
    
    def test_post_has_publication_date(self):
        print(self.post.publication_date)
        self.assertIsNotNone(self.post.publication_date)
    
    def test_post_has_comment_at(self):
        self.assertIsNotNone(self.comment1.comment_at)
        
    def test_comment_has_post(self):
        self.assertEqual(self.post,self.comment1.post)
        self.assertEqual(self.post,self.comment2.post)
        
    def test_comment_has_user(self):
        self.assertEqual(self.comment1.user, self.author1)
        
    def test_comment(self):
        self.assertEqual(self.comment1.comment, 'Good')
        self.assertEqual(self.comment2.comment, 'Nice')
        
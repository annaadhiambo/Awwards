from django.test import TestCase
from .models import Post, Username
from django.contrib.auth.models import User
from datetime import datetime
from django.core.files.uploadedfile import SimpleUploadedFile


filename = '/home/moringa/Desktop/Awwards/media/default.jpg'


# Create your tests here.
class TestPostModel(TestCase):
    def setUp(self):
        self.user = User(username="testuser",password="adminpass")
        self.user.save()
        filename = '/home/moringa/Desktop/Awwards/media/default.jpg'
        self.post = Post(
            image= SimpleUploadedFile(name='test_image.jpg', content=open(filename, 'rb').read(), content_type='image/jpeg'),
            title="test title",
            description="test description",
            image_url="http://test.image.url.com",
            author=self.user,
            date_posted=datetime.now()
        )
    
    def test_post_create(self):
        self.post.save()
        query = Post.objects.all()
        self.assertTrue(len(query)>0)
    
    def test_post_update(self):
        self.post.save()
        test_title = 'updated_title'
        self.post.title = test_title
        self.post.save()
        self.assertTrue(self.post.title,test_title)

    def test_delete_post(self):
        self.post.save()
        self.post.delete()
        query =Post.objects.all()
        self.assertIs(len(query),0)
    
    def test_post_is_instance(self):
        self.post.save()
        query = Post.objects.all()
        self.assertIsInstance(query[0],Post)


class TestUsernameModel(TestCase):
    def setUp(self):
        self.title ='test title'
        self.description ="Lorem ipsum dolor sit amet"

        self.image= SimpleUploadedFile(name='test_image.jpg', content=open(filename, 'rb').read(), content_type='image/jpeg')
        self.username = Username(
            image=self.image,
            title =self.title,
            description=self.description
        )
    

    def test_username_create(self):
        self.username.save_username()
        query = Username.objects.all()
        self.assertTrue(len(query)>0)
    
    def test_username_update(self):
        self.username.save_username()
        test_description = 'updated desc'
        self.username.description = test_description
        self.username.update_username()
        self.assertTrue(self.username.description,test_description)

    def test_delete_username(self):
        self.username.save_username()
        self.username.delete_username()
        query =Username.objects.all()
        self.assertIs(len(query),0)
    
    def test_username_is_instance(self):
        self.username.save()
        query = Username.objects.all()
        self.assertIsInstance(query[0],Username)


    
    
from django.test import TestCase
from .models import Post, Username
from django.contrib.auth.models import User
from datetime import datetime
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.
class PostTestClass(TestCase):
    def setUp(self):
        self.user = User(username="testuser",password="adminpass")
        self.user.save()
        self.post = Post(
            image= SimpleUploadedFile(name='test_image.jpg', content=open('..templates/default.jpg', 'rb').read(), content_type='image/jpeg'),
            title="test title",
            description="test description",
            image_url="http://test.image.url.com",
            author=user,
            date_posted=datetime.now()
        )
    
    def test_user_create(self):
        self.post.save()
        query = Post.objects.all()
        self.assertTrue(len(query)>1)


    
    
from django.shortcuts import render
from .models import Post


posts = [
    {
        'image':'',
        'title':'Delani',
        'description':'An application that allows you get to send Our approach unifies design, development and product management to create exceptional products.',
        'image_url':'',
        'author':'Anna Adhiambo',
        'date_posted':'October 24,2020',
    },
    {
        'image':'',
        'title':'Gallery',
        'description':'An application that allows you have new fashion in town',
        'image_url':'',
        'author':'Anna Adhiambo',
        'date_posted':'October 24,2020'
    },
    {
        'image':'',
        'title':'Pizza',
        'description':'An application that allows you have new fashion in town',
        'image_url':'',
        'author':'Anna Adhiambo',
        'date_posted':'October 24,2020'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'photo/home.html', context)




from django.shortcuts import render
from .models import Post
import random


def home(request):
    try: 
        posts= Post.objects.all()
        posts = posts[::-1]
        one_post = random.randint(0, len(posts)-1)
        random_post= posts[one_post]
        print(random_post)
    except Post.DoesNotExist:
        posts = None

    return render(request, 'photo/home.html', locals())


def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_username = Username.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'photo/search.html',{"message":message,"username": searched_username})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photo/search.html',{"message":message})





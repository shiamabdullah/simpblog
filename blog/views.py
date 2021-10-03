from django.http.response import HttpResponse,HttpResponseNotFound
from django.shortcuts import render
import datetime
from blog.models import Post
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.
def post_list(request):  
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    me=User.objects.get(username='shiam')
    postsbyme = Post.objects.filter(author=me)
    return render(request, 'blog/post_list.html', {'posts': posts, 'postShiam' : postsbyme})

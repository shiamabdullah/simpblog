from django.http.response import HttpResponse,HttpResponseNotFound
from django.shortcuts import render
import datetime

# Create your views here.
def post_list(request):  
    return render(request, 'blog/post_list.html', {})

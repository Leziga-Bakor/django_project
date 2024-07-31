from django.shortcuts import render
from .models import Post

posts = [
    {
        'author':'James',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted':'May 20, 2024'
    },
    {
        'author':'Ann',
        'title': 'Blog Post 2',
        'content':'Second post content',
        'date_posted':'June 7, 2024'
    }
]

# Create your views here.
def home(request):
    context = { 
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
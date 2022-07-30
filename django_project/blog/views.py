from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Dummy data

posts = [
    {
        'author' : 'IvoZ',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'July 28, 2022'
    },
    {
        'author' : 'AnaZ',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'July 29, 2022'
    }
]

def home(request):
    context = {
        'posts' : posts
        }
    return render(request, 'blog/home.html', context)

def about(request):
    title = {
        'title' : 'About'
    }
    return render(request, 'blog/about.html', title)
    

from django.shortcuts import render
from django.http import HttpResponse

posts = [
  {
    'author': 'Dave Regg',
    'title': 'Blog Post 1',
    'content': 'My first post :)',
    'date_posted': 'December 26, 2019'
  },
  {
    'author': 'Cynthia Harvey',
    'title': 'Blog Post 2',
    'content': 'My second post!',
    'date_posted': 'December 26, 2019'
  },
  {
    'author': 'Dave Regg',
    'title': 'Blog Post 3',
    'content': 'My third post :[',
    'date_posted': 'December 26, 2019'
  }
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html')
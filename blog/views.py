from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {'author': 'Tunde-Fadipe',
     'title': 'new blog',
     'content' : 'teaching and learning django',
     'date_posted': '23-08-2022'
     },
    {'author': 'Pelumi_o',
     'title': 'small vlog',
     'content' : ' new content ofteaching and learning django',
     'date_posted': '13-05-2012'
     }
]
def home(request):
    context ={'posts' : posts}
    return render(request, 'blog/home.html', context)
def about(request):
    context ={'title' : 'about'}
    return render(request, 'blog/about.html', context)
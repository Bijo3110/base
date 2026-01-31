from django.shortcuts import render
from django.views import View
from .models import Blog
from .forms import BlogForm

# Create your views here.

class HomeView(View):

    def get(self, request):
        blogs = Blog.objects.all()
        form = BlogForm()
        context = {
            'blogs' : blogs,
            'form' : form
        }
        return render(request, 'home.html', context)
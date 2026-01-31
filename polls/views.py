from django.shortcuts import render
from django.views import View
from .models import Blog

# Create your views here.

class HomeView(View):

    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            'blogs' : blogs
        }
        return render(request, 'home.html', context)
from django.shortcuts import render
from django.views import View
from .models import Blog

# Create your views here.

class HomeView(View):

    def get(self, request):
        blog = Blog.objects.all()
        context = {
            'blog' : blog
        }
        return render(request, 'home.html', context)
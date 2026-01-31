from django.http import HttpResponse
from django.shortcuts import render, redirect
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
    
    def post(self, request):
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return HttpResponse("Form Is Invaild")

class BlogDetail(View):
    def get(self, request, pk):
        blog = Blog.objects.get(id=pk)
        context = {
            'blog' : blog
        }
        return render(request, 'blog_details.html', context)
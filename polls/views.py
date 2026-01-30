from django.shortcuts import render
from django.views import View
from .models import Question

# Create your views here.

class HomeView(View):

    def get(self, request):
        questions = Question.objects.all()
        context = {
            'questions' : questions
        }
        return render(request, 'home.html', context)
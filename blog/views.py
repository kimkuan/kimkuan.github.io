from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects #쿼리셋(객체들의 목록) #메소드(객체들을 처리)
    return render(request, 'home.html', {'blogs' : blogs})

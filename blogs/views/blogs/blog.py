from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from blogs.models import Blog


# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

class BlogView(View):
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()

        context = {'blogs':blogs}
        return render(request, 'blogs/blogs.html', context)

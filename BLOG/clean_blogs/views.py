from django.shortcuts import render
from django.views import generic
from datetime import datetime
from clean_blogs.models import Contact, FilesUpload, BlogPost, Projects
from django.contrib import messages

# Create your views here.
def post(request):
    return render(request, 'post.html')

def books(request):
    obj = FilesUpload.objects.all()
    context = {
        'object': obj, 
    }
    return render(request, 'books.html', context)

def projects(request):
    obj = Projects.objects.all()
    context = {
        'object': obj, 
    }
    return render(request, 'projects.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(
            name=name, 
            email=email,
            desc=desc,
            date=datetime.today()
            )
        contact.save()
        messages.success(request, 'Message has been sent!')
    return render(request, 'contact.html')

class BlogPostList(generic.ListView):
        queryset = BlogPost.objects.filter(status=1).order_by('-created_on')

class BlogPostDetail(generic.DetailView):
    model = BlogPost
    template_name = 'post.html'
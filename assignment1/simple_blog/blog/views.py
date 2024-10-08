from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from .models import Post, Comment
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all().values()
    template = loader.get_template('post_list.html')
    context = {
        "posts": posts,
    }

    return HttpResponse(template.render(context, request))

def post_details(request, id):
    post = Post.objects.get(id=id)
    template = loader.get_template('post_details.html')
    context = {
        "post": post,
        "comments": None,
    }

    return HttpResponse(template.render(context, request))

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_details', post.id)
    else: 
        form = PostForm()
    template = loader.get_template('post_form.html')
    context = {
        "form": form,
    }
    return HttpResponse(template.render(context, request))

def post_edit(request, id):
    post = Post.objects.get(id)
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_detail', id = id)
    
    return HttpResponse()

def post_delete(request, id):
    post = Post.objects.get(id = id)
    if request.user == post.author:
        post.delete()
    return redirect('post_list')

def comment_list(request, id):
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post=post)
    template = loader.get_template('post_details.html')
    context = {
        "post": post,
        "comments": comments,
    }
    return HttpResponse(template.render(context, request))


def comment_create(request, id):
    post = Post.objects.get(id=id)
    
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            comment = Comment(content=content, author=request.user, post=post)
            comment.save()
            return redirect("comment_list", id)

    return redirect("comment_list", id) 

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render(request=request))
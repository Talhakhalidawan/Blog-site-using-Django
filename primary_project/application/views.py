from django.shortcuts import render , HttpResponse , redirect
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by("-dateCreated")
    context = {
        "post" : posts,
    }
    return render(request , "index.html" , context)

def createPost(request):
    if request.method == "POST":
        name = request.POST.get("poster-name")
        time = "posting-time" in request.POST
        upImage_caption = request.POST.get("upImage-caption")
        image = request.FILES.get("image")
        downImage_caption = request.POST.get("downImage-caption")
        post = Post.objects.create(name = name , upImageCaption = upImage_caption , downImageCaption = downImage_caption , date = time , image = image)
        post.save()
        return render(request , "back.html")
        
    return render(request , "create-post.html")

def about(request):
    return render(request , "about.html")

def logout(request):
    return render(request , "logout.html")

def admin(request):
    posts = Post.objects.all().order_by("-dateCreated")
    context = {
        "post" : posts,
    }
    return render(request , "admin.html" , context)

def update(request , uid):
    post = Post.objects.get(uid = uid)
    if request.method == "POST":
        name = request.POST.get("poster-name")
        time = "posting-time" in request.POST
        upImage_caption = request.POST.get("upImage-caption")
        image = request.FILES.get("image")
        downImage_caption = request.POST.get("downImage-caption")
        
        post.name = name
        post.upImageCaption = upImage_caption
        post.downImageCaption = downImage_caption
        post.date = time
        
        if image == None:
            pass
        else :
            post.image = image
            
        post.save()
        return render(request , "back.html")
    context = {
        "post" : post,
    }
    return render(request , "update.html" , context)

def delete(request , uid):
    post = Post.objects.get(uid = uid)
    post.delete()
    return render(request , "back.html")
from django.shortcuts import render,redirect,get_object_or_404
from .models import *

def create_user(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        image = request.FILES.get('image')
        User.objects.create(first_name=first_name,last_name=last_name,email=email,age=age,image=image)
        return redirect('home')
    return render(request,'cr_user.html')


def user_get_by_id(request, id):
    users = get_object_or_404(User, id=id)
    posts = Post.objects.filter(user_id=users)
    return render(request, 'user_by_id.html', {'users': users, 'posts': posts})



def user_list(request):
    users = User.objects.all()
    return render (request,'postuser.html',{'users': users})

def update_user(request,id):
    users = get_object_or_404(User,id=id)
    if request.method == 'POST':
        users.first_name = request.POST.get('first_name')
        users.last_name = request.POST.get('last_name')
        users.email = request.POST.get('email')
        users.age = request.POST.get('age')
        users.image = request.FILES.get('image')
        
        users.save()
        return redirect('list-user')
       
    return render(request,'cr_user.html')

def delete_user(request,id):
    users = get_object_or_404(User,id=id)
    users.delete()
    return redirect('list-user')



def create_post(request):
    users=User.objects.all()
    if request.method=='POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user_id = request.POST.get('user_id')
        video = request.FILES.get('video')
        Post.objects.create(title=title,description=description,user_id=User.objects.get(id=user_id),video=video)
        return redirect('home')
    return render(request,'cr_post.html',{'users': users})


def post_list(request):
    posts = Post.objects.all()
    users=User.objects.all()
    title = request.GET.get('title')
    if title:
        posts=posts.filter(title__icontains=title)
    movid = request.GET.get('movid')
    if movid:
        posts=posts.filter(id=movid)
    uservideo = request.GET.get('uservideo')
    if uservideo:
        posts = posts.filter(user_id=uservideo)
    titlo = request.GET.get('titlo')
    if titlo:
        posts = posts.filter(id=titlo)


    return render (request,'postlist.html',{'posts': posts, 'users': users})


def update_post(request,id):
    posts = get_object_or_404(Post,id=id)
    users = User.objects.all()
    if request.method == 'POST':
        posts.title = request.POST.get('title')
        posts.description=request.POST.get('description')
        user_id=request.POST.get('user_id')
        posts.user_id = User.objects.get(id=user_id)
        posts.video=request.FILES.get('video')
        
        posts.save()
        return redirect('list-post')
       
    return render(request,'cr_post.html',{'users': users})

def delete_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.delete()
    return redirect('list-post')

def post_get_by_id(request, id):
    posts = get_object_or_404(Post, id=id)
    return render(request, 'post_by_id.html', {'posts': posts})




def home(request):
    return render(request,'home.html')
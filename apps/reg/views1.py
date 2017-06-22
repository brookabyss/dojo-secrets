from django.shortcuts import render, redirect, reverse
from .models import Users
from ..secrets.models import Post
from django.contrib import messages

def index(request):
    return render(request,'reg/index.html')

def register(request):
    if request.method=="POST":
        #if the fields pass the vaildation the  object will be created in the database
        if Users.objects.registration(request):
            request.session['current_user']=request.POST['first_name']
            request.session['current_user_id']=Users.objects.get(email=request.POST['email']).id
            messages.success(request,'Successfully registered')
            return redirect(reverse('secrets:secrets'))
            # return render(request,'reg/secrets.html', context)
        else:
            return redirect('/')
    else:
        return redirect('/')

def login(request):

    if request.method=="POST":
        login=Users.objects.login(request)
        request.session['current_user_id']=Users.objects.get(email=request.POST['email']).id
        if login==False:
            return redirect('/')
        else:
            request.session['current_user']=login.first_name
            messages.success(request,'Successfully logged in')
            posts=Post.objects.all()[:3]
            context={
                'posts':posts
            }
            # return redirect(reverse('secrets:secrets'))
            return render(request,'secrets/secrets.html', context)

    else:
        return redirect('/')

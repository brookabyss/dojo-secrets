from django.shortcuts import render, redirect, reverse
from .models import Post
from ..reg.models import Users
from datetime import datetime
from django.db.models import F
def show(request):
    posts=Post.objects.all()[:5]
    context={
        "posts":posts
    }
    return render(request,'secrets/secrets.html', context)

def create_post(request):
    if request.method=="POST":
        content=request.POST['comment']
        user_id=Users.objects.get(id=request.session['current_user_id'])
        Post.objects.create(content=content, user_id=user_id)
        posts=Post.objects.all()[:3]
        context={
            'posts': posts,
        }
        return render(request,"secrets/secrets.html", context)
    else:
        return redirect(reverse('secrets:secrets'))
def like(request,post_id):
    current_user_id=request.session['current_user_id']
    user=Users.objects.get(id=current_user_id)
    post=Post.objects.get(id=post_id)
    if post.user_likes.filter(id=current_user_id).count()>0:
        Post.objects.filter(id=post_id).update(total_likes=F('total_likes')-1)
        post.user_likes.remove(user)
        return redirect(reverse('secrets:secrets'))
    else:
        post.user_likes.add(user)
        Post.objects.filter(id=post_id).update(total_likes=F('total_likes')+1)
    # if like.objects.filter(post_id=post_id).count()<1:
    #     Like.objects.create(post_id=post_id,user_id=user_id)
    #     like=Like.objects.get(post_id=post_id).update(total_likes=F('total_likes')+1)
    # else:
    #     Like.objects.get(post_id=post_id).update(total_likes=F('total_likes')+1)
    # likes=Like.objects.all()
    return redirect(reverse('secrets:secrets'))

def popular(request):
    posts=Post.objects.all().order_by('-total_likes')
    context={
        "posts":posts,
        'user': request.session['current_user_id']
    }
    return render(request,'secrets/popular.html', context)


def delete(request,post_id):
    try:
        post=Post.objects.get(id=post_id)
        post.delete()
        return redirect(reverse('secrets:popular'))
    except:
        return redirect(reverse('secrets:popular'))

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect

from .forms import PostForm
from .models import Post

#-------------------------------------- index() _________________________________
def index(request):
    context = {
        'posts':Post.objects.all().order_by('-id')
    }

    return render(request,"posts/index.html",context = context)



#-------------------------------------- detail() _________________________________
def detail(request,id):
    post =get_object_or_404(Post, id=id)

    context = {
        'post':post
    }

    return render(request,"posts/detail.html",context=context)


#-------------------------------------- create_post() _________________________________
@login_required(login_url='/')
def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save()
        return HttpResponseRedirect(post.get_absolute_url())


    context = {
        'form':form
    }

    return render(request,"posts/create.html",context=context )

#-------------------------------------- delete_post() _________________________________
@login_required(login_url='/')
def delete_post(request,id):
    post = get_object_or_404(Post, id=id)
    post.delete()

    return redirect('/')


#-------------------------------------- update_post() _________________________________
@login_required(login_url='/')
def update_post(request,id):
    post=get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form':form
    }


    return render(request,'posts/create.html',context=context)






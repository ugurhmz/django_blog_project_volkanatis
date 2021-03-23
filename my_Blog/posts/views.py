from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect

from .forms import PostForm
from .models import Post


def index(request):
    context = {
        'posts':Post.objects.all().order_by('-id')
    }

    return render(request,"posts/index.html",context = context)




def detail(request,id):
    post =get_object_or_404(Post, id=id)

    context = {
        'post':post
    }

    return render(request,"posts/detail.html",context=context)



@login_required(login_url='/')
def create_view(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save()
        return HttpResponseRedirect(post.get_absolute_url())


    context = {
        'form':form
    }

    return render(request,"posts/create.html",context=context )


@login_required(login_url='/')
def delete_view(request,id):
    post = get_object_or_404(Post, id=id)
    post.delete()

    return redirect('/')










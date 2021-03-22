from django.shortcuts import render



def index(request):
    context = {
        'message':'bu benim ilk mesajım',
        'message2':'bu benim ikinci mesajım'
    }

    return render(request,"posts/index.html",context = context)
from django.shortcuts import get_object_or_404, render
from .models import Post   #Post modelinin içe aktarımı

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')   #En yeniden eskiye doğru post objelerini sırala
    context = {
        'posts' : posts #Veriyi şablona gonder
    }

    return render(request, 'home.html', context)

def post_detail(request , pk): 
    post = get_object_or_404(Post , pk=pk)  #ID si verilen yazııy bul (pk) bulmazsa 404 yazsın 
    context = {
        'post' : post
    }

    return render(request, 'post_detail.html', context)


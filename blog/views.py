from django.shortcuts import render

def post_list(request): #вызывается при начальной странице
    return render(request, 'blog/post_list.html', {})

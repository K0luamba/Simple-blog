from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request): #вызывается при начальной странице
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts}) #в {} то, что передаем как параметр в отображение страицы

def post_detail(request, pk): #при передаче запроса сохраняется значение pk
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post}) #передаем только один пост
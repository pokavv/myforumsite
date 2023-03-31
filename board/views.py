from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.core.paginator import Paginator

from .models import Post

# index.html 요청하는 index 함수
def index(request):
    return render(request, 'board/index.html')

# post-list.html 요청하는 post_list 함수
def post_list(request):
    # 모든 Post를 가져와서 posts에 저장
    posts = Post.objects.all()
    curr_page_number = request.GET.get('page')
    paginator = Paginator(posts, 6)
    
    if curr_page_number is None:
        curr_page_number = 1
    
    page = paginator.page(curr_page_number)
    
    # post-list.html을 열 때, posts도 함께 가져오기
    return render(request, 'board/post-list.html', {'posts':posts})

# posting
def posting(request, pk):
    # primary_key(pk)를 이용해 하나의 posting 검색
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        raise Http404()
    
    post = get_object_or_404(Post, id=pk)
    context = {'post': post}
    
    # posting.html을 열 때, post라는 이름으로 가져옴
    return render(request, 'board/posting.html', context)

# new post write
def write(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save()
            return redirect('posting', post_id=new_post.id)
    else:
        post_form = PostForm()
    return render(request, 'board/write.html', {'form': post_form})

# remove post
def remove(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')
    else:
        return render(request, 'board/post_confirm_delete.html', {'post':post})

def update(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('posting', post_id=post.pk)
    else:
        post_form = PostForm(instance=post)
    
    post_form = PostForm(instance=post)
    return render(request, 'board/write.html', {'form': post_form})
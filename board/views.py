from django.shortcuts import render, redirect

from .models import Post

# index.html 요청하는 index 함수
def index(request):
    return render(request, 'board/index.html')

# post-list.html 요청하는 post_list 함수
def post_list(request):
    # 모든 Post를 가져와서 posts에 저장
    posts = Post.objects.all()    
    # post-list.html을 열 때, posts도 함께 가져오기
    return render(request, 'board/post-list.html', {'posts':posts})

# posting
def posting(request, pk):
    # primary_key(pk)를 이용해 하나의 posting 검색
    post = Post.objects.get(pk=pk)
    # posting.html을 열 때, post라는 이름으로 가져옴
    return render(request, 'board/posting.html', {'post':post})

# new post write
def write(request):
    if request.method == 'POST':
        if request.POST['post_image']:
            write = Post.objects.create(
                postname = request.POST['postname'],
                post_image = request.POST['post_image'],
                contents = request.POST['contents'],
            )
        return redirect('/list/')
    return render(request, 'board/write.html')
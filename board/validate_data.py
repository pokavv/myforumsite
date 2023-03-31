from .models import Post

def validate_post():
    # 모든 포스트 데이터 가져오기
    posts = Post.objects.all()
    
    # 각각의 포스트 데이터를 보면서 내용 적합성 체크하기
    for post in posts:
        if '&' in post.contents:
            print(post.id, '번 글에 &가 있습니다.')
            
            # 만약 적합성을 만족하지 않으면 삭제
            post.contents = post.contents.replace('&', '')

            # 데이터 저장
            post.save()
        
        if post.dt_modified < post.dt_created:
            print(post.pk, '번 글의 수정일이 생성일보다 과거입니다.')
            post.save()
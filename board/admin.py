from django.contrib import admin

from .models import Post

# admin이 Post에 접근 가능
admin.site.register(Post)
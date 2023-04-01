from django.urls import path

# image upload
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.IndexRedirectView.as_view(), name='index'),
    path('posts/', views.PostListView.as_view(), name='post_list'),
    path('posts/new/', views.PostCreateView.as_view(), name='write'),
    path('posts/<int:post_id>/', views.PostDetailView.as_view(), name='posting'),
    path('posts/<int:post_id>/edit/', views.PostUpdateView.as_view(), name='update'),
    path('posts/<int:post_id>/delete/', views.PostDeleteView.as_view(), name='delete'),
]

# image url setting
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
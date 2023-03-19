from django.urls import path

# image upload
from django.conf import settings
from django.conf.urls.static import static

from board.views import index, post_list, posting
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.post_list, name='post_list'),
    path('list/<int:pk>/', posting, name='posting'),
    path('list/write/', views.write, name='write'),
]

# image url setting
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include

# from bookmark.views import BookmarkLV, BookmarkDV
# -->

from mysite.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/-> 홈페이지에 값을 ㄴ넣을것이다
    path('', HomeView.as_view(),name='home'),

    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    # path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail'),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('blog/', include('blog.urls', namespace='blog')),
    
    ]

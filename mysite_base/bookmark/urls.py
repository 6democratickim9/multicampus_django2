from django.urls import path

from bookmark.views import BookmarkLV, BookmarkDV

app_name='bookmark'

urlpatterns = [
    path('',BookmarkLV.as_view(),name='id'),
    path('<int:pk>',BookmarkDV.as_view(),name='detail'),
   
]

from django.urls import path,include
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeletelView

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'), #url will be<app>/<model>_<viewtype(eg. listview)>.html
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),#calling PostDetailView as post/primarykey- id as integer url:/blog/post_detail.html
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),#calling PostUpdateView as post/primarykey/- id as integer url:/blog/post_detail/update.html
    path('post/<int:pk>/delete/',PostDeletelView.as_view(),name='post-delete'),#calling PostDeletelView as post/primarykey/- id as integer url:/blog/post_detail/delete.html
    path('post/new/',PostCreateView.as_view(),name='post-create'),#calling PostCreatelView as post/primarykey- id to create new posts url:/blog/post/form
    path('about/',views.about,name='blog-about'),
    
]
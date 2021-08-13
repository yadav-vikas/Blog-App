from django.urls import path,include
from . import views
from .views import PostListView

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'), #url will be<app>/<model>_<viewtype(eg. listview)>.html
    path('about/',views.about,name='blog-about'),
    
]
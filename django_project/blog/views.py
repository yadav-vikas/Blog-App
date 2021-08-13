from django.shortcuts import render
from .models import  Post
from django.views.generic import ListView


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    """Home page showing all the posts, so we use list views to show all posts
    Types of Class Based views :
    class based views ---------
	list views   (list of subs on youtube)
	detail views (click on one of subs on list)	
	create views (create video)
	update views (update video)
	delete views (delete video)
    Args:
        ListView ([type]): [description]
    """
    model = Post
    template_name = 'blog/home.html' #app/model_viewtype.html
    context_object_name = 'posts' # calling each posts as views
    ordering = ['-date_posted']  # order of post -date_posted will be descending and date_posted will be ascending('-'sign)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

    
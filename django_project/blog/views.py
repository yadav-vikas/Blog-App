from django.shortcuts import render,get_object_or_404
from .models import  Post
from django.contrib.auth.models import  User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


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
    paginate_by = 5 # adding paginator object for pagination 5 post per page

class UserPostListView(ListView):
    """showing users profiles and their posts
    Args:
        ListView ([type]): [description]
    """
    model = Post
    template_name = 'blog/user_posts.html' #app/model_viewtype.html
    context_object_name = 'posts' # calling each posts as views
    paginate_by = 5 # adding paginator object for pagination 5 post per page

    def get_queryset(self):
        """[We are first checking if the user exist from the User model by passing object get_object_or_404 if the user exists the
        then to show their posts we are passing a query to short by date posted descending order]

        Returns:
            [user profile]: [we are returning the user if exist or throwing HTTP 404 error]
        """
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    """Home page showing all the posts, so here we are showing each posts details using DetailView 
    Types of Class Based views :
    class based views ---------
	list views   (list of subs on youtube)
	detail views (click on one of subs on list)	
	create views (create video)
	update views (update video)
	delete views (delete video)
    Args:
        DetailView ([type]): [description]
    """
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    """Home page showing all the posts, so here we are creating new posts  using Createview 
    Types of Class Based views :
    class based views ---------
	list views   (list of subs on youtube)
	detail views (click on one of subs on list)	
	create views (create video)
	update views (update video)
	delete views (delete video)
    LoginRequiredMixin - this will help us user to restrict to access or create posts if the user is not logged in.
    Args:
        CreateView ([type]): [description]
    """
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Home page showing all the posts, so here we are updating the posts that already exists

    Types of Class Based views :
    class based views ---------
	list views   (list of subs on youtube)
	detail views (click on one of subs on list)	
	create views (create video)
	update views (update video)
	delete views (delete video)
    LoginRequiredMixin - this will help us user to restrict to access or create posts if the user is not logged in.
    UserPassesTestMixin - this will help user to restrict to update/delete posts that are specific to that user
    
    Args:
        UpdateView - we are using UpdateView class to update the user posts
        LoginRequiredMixin - this will help us user to restrict to access or create posts if the user is not logged in.
        UserPassesTestMixin - this will help user to restrict to update/delete posts that are specific to that user
    
    """
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user # providing author for that logged in user in creating new posts
        return super().form_valid(form)

    def test_func(self):
        """function to check if a particular post belongs to that author/user

        Returns:
            [if False]: HTTP 403 Forbidden 
        """
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False

class PostDeletelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Home page showing all the posts, so here we are deleting posts after checking that post belongs to that user 
    Types of Class Based views :
    class based views ---------
	list views   (list of subs on youtube)
	detail views (click on one of subs on list)	
	create views (create video)
	update views (update video)
	delete views (delete video)
    Args:
        DetailView ([type]): [description]
    """
    model = Post
    success_url = '/'

    def test_func(self):
        """function to check if a particular post belongs to that author/user

        Returns:
            [if False]: HTTP 403 Forbidden 
        """
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

    
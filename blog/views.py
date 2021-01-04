from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post

# from django.http import HttpResponse
# Create your views here.


# handle traffic from the home page
def home(request):
    context = {
        # 'posts': posts
        "posts": Post.objects.all
    }
    return render(request, "blog/home.html", context)


# return HttpResponse('<h1>Blog Home</h1>')


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    # order of post in home page -date posted is the newest is on top
    # ordering = ["-date_posted"]
    # pagination
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    # order of post in home page -date posted is the newest is on top
    ordering = ["-date_posted"]
    # pagination
    paginate_by = 5

    def get_queryset(self):
        # kwargs query parameter
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Post


# need login to create post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        # set instance as current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

        # need login to update post


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        # set instance as current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # check if the author is the user of the post
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # if success send to home page
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        # check if the author is the user of the post
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, "blog/about.html", {"title": "About"})

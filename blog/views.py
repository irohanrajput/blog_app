from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'all_posts_list'
    # if in case the context object name is not defined, the default name is object_list

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ('title','body')

    

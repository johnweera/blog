from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'


class AuthorPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/author.html'
    

class PostDetailView(UpdateView):
    model = Post
    fields = ['title', 'body', 'author']
    template_name = 'blog/post_detail.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'body', 'youtube']
    template_name = 'blog/post_update.html'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:author')
    template_name = 'blog/post_confirm_delete.html' 


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('blog:author')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PostForm()
        context = {
            'form':form
        }

    return render(request, 'blog/post_form.html', context)

#####################################################################


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'body']
#     form = PostForm

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


# class PostUpdateView(LoginRequiredMixin, UpdateView):
#     model = Post
#     fields = ['title', 'body']

#     def get_queryset(self):
#         return Post.objects.filter(author=self.request.user)

# class PostDeleteView(LoginRequiredMixin, DeleteView):
#     model = Post
#     success_url = reverse_lazy('blog:list')

#     def get_queryset(self):
#         return Post.objects.filter(author=self.request.user)
    

# class PostListView(LoginRequiredMixin, ListView):
#     model = Post
#     template_name = 'blog/post_list.html'
    
#     def get_queryset(self):
#         return Post.objects.filter(author=self.request.user)    
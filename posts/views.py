from django.shortcuts import get_object_or_404, render
from posts.models import Post
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from posts.forms import PostForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostSearchView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            posts = Post.objects.filter(title__icontains=query)
            if not posts.exists():
                messages.error(self.request, 'Nenhuma postagem encontrada.')
            return posts
        return Post.objects.all()
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_object(self):
        return Post.objects.get(pk=self.kwargs['pk'])

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        messages.success(self.request, 'O post foi criado com sucesso')
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    context_object_name = 'form'
    def get_success_url(self):
        return reverse_lazy('post-detail', args=[self.object.pk])

    def form_valid(self, form):
        messages.success(self.request, 'O post foi atualizado com sucesso')
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post-list')

    def get_success_url(self):
        messages.error(self.request, 'O post foi deletado com sucesso')
        return super().get_success_url()



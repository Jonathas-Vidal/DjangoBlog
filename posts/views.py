
from posts.models import Post
from django.contrib import messages
from django.urls import reverse_lazy
from posts.forms import PostForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden

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

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'O post foi criado com sucesso')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'create'
        return context

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    context_object_name = 'form'
    
    def get_success_url(self):
        return reverse_lazy('post-detail', args=[self.object.pk])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'update'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'O post foi atualizado com sucesso')
        return super().form_valid(form)



@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post-list')

    def get_success_url(self):
        messages.error(self.request, 'O post foi deletado com sucesso')
        return super().get_success_url()



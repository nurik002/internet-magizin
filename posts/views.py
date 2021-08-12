from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from posts.forms import PostCommentFormModel
from posts.models import PostModel


class PostListView(ListView):
    template_name = 'blog-fullpage.html'
    queryset = PostModel.objects.order_by('-pk')
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = PostModel


class PostCommentCreateView(CreateView):
    form_class = PostCommentFormModel

    def get_success_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        form.instance.post = get_object_or_404(PostModel, pk=pk)
        return super().form_valid(form)

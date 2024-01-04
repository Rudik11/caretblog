from django.shortcuts import render, get_object_or_404, redirect
from .forms import CarpetPostForm
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import CarpetPost

def post_create(request):
    if request.method == 'POST':
        form = CarpetPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = CarpetPostForm()
    return render(request, 'carpets/post_form.html', {'form': form, 'action': 'Create'})

def post_update(request, post_id):
    post = get_object_or_404(CarpetPost, pk=post_id)
    if request.method == 'POST':
        form = CarpetPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CarpetPostForm(instance=post)
    return render(request, 'carpets/post_form.html', {'form': form, 'action': 'Update'})

def post_delete(request, post_id):
    post = get_object_or_404(CarpetPost, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'carpets/post_confirm_delete.html', {'post': post})

def post_list(request):
    posts = CarpetPost.objects.all()
    return render(request, 'carpets/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(CarpetPost, pk=post_id)
    return render(request, 'carpets/post_detail.html', {'post': post})
# carpets/views.py

class PostDeleteView(DeleteView):
    model = CarpetPost
    template_name = 'carpets/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
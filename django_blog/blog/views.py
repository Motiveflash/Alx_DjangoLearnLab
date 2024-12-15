from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileUpdateForm, CommentForm
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils import timezone  # Import timezone to handle updated_at field


# Register View - User Registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in!')
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            messages.error(request, 'Error creating account. Please try again.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'blog/register.html', {'form': form})

# Login View - User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Welcome back!')
            return redirect('home')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    
    return render(request, 'blog/login.html', {'form': form})

# Logout View - User Logout
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')

# Profile View - User Profile Update
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')  # Redirect to the profile page after updating
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    return render(request, 'blog/profile.html', {'form': form})

# Home View - Displaying the list of posts with pagination
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

# ListView - Display all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Template for listing posts
    context_object_name = 'posts'
    ordering = ['-created_at']  # Order by most recent
    paginate_by = 10  # Pagination: show 10 posts per page

# DetailView - Display a single blog post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Template for viewing a post

# CreateView - Allow authenticated users to create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'  # Template for creating a post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the logged-in user as the author
        return super().form_valid(form)

# UpdateView - Allow post authors to edit their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'  # Template for editing a post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure the author remains the same
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can edit

# DeleteView - Allow post authors to delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # Template for deleting a post
    success_url = reverse_lazy('post-list')  # Redirect to the post list after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Only the author can delete


# View for displaying post details with comments
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()  # Retrieve all comments related to this post
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('post-detail', pk=post.pk)  # Redirect back to the post detail page
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

# CommentCreateView - Class-based view to create a new comment
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user  # Set the logged-in user as the author
        messages.success(self.request, 'Your comment has been added!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

# Edit Comment View
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)  # Only allow the author to edit the comment

    def form_valid(self, form):
        form.instance.updated_at = timezone.now()  # Update the time when the comment is modified
        messages.success(self.request, 'Your comment has been updated!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

# Delete Comment View
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)  # Only allow the author to delete the comment

    def get_success_url(self):
        messages.success(self.request, 'Your comment has been deleted!')
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})

from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileForm 

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class LoginView(LoginView):
    pass

class LogoutView(LogoutView):
    next_page = reverse_lazy('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'relationship_app/register.html', context)


@login_required
def profile_view(request):
    profile = request.user.userprofile  # Ensure `userprofile` exists on `User`
    context = {"profile": profile}
    return render(request, "relationship_app/profile.html", context)

@login_required
def profile_edit_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user.userprofile)
    return render(request, "relationship_app/profile_edit.html", {"form": form})


# Check if user is an admin
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Check if user is a librarian
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# Check if user is a member
def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

def error_page(request):
    return HttpResponse("You do not have permission to view this page.")


# Custom Permission Logic
def check_role(role):
    def has_role(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return has_role

# Views using `check_role`
@user_passes_test(check_role('Admin'), login_url='/error/')
def admin_view(request):
    return HttpResponse("Welcome to the Admin Page!")

@user_passes_test(check_role('Librarian'), login_url='/error/')
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian Page!")

@user_passes_test(check_role("Member"), login_url='/error/')
def member_view(request):
    return HttpResponse("Welcome to the Member Page!")

from django.shortcuts import render
from django.shortcuts import redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from .forms import ProfileForm

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class LoginView(LoginView):
    pass

class LogoutView(LogoutView):
    next_page = reverse_lazy(login)

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
    profile = request.user.user_profile
    context = {"profile": profile}
    return render(request, "profile.html", context)

@login_required
def profile_edit_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user.user_profile)
    return render(request, "profile_edit.html", {"form": form})


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


# View accessible only to Admins
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


# View accessible only to Librarians
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


# View accessible only to Members
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



# Custom Permission Logic
def check_role(role):
    def has_role(user):
        return user.is_authenticated and user.profile.role == role
    return has_role

@user_passes_test(check_role('Admin'), login_url='/error/')
def admin_view(request):
    return HttpResponse("Welcome to the Admin Page!")

@user_passes_test(check_role('Librarian'), login_url='/error/')
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian Page!")

@user_passes_test(check_role("Member"), login_url='/error/')
def member_view(request):
    return HttpResponse("Welcome to the Member Page!")


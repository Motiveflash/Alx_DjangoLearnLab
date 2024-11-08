from django.shortcuts import render
from django.shortcuts import redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

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
    next_page = reverse_lazy('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

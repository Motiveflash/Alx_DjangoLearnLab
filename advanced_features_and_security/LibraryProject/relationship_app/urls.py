from .views import list_books
from .views import add_book, edit_book, delete_book
from .views import LibraryDetailView
from .views import register
from .views import LogoutView
from .views import LoginView
from . import views
from django.urls import path


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),

    path('library/', LibraryDetailView.as_view(), name='library'),
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path("register/", views.register, name="register"),

    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.profile_edit_view, name="profile_edit"),


    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    path('admin_page/', views.admin_view, name='admin_page'),
    path('librarian_page/', views.librarian_view, name='librarian_page'),
    path('member_page/', views.member_view, name='member_page'),
    path('error/', views.error_page, name='error_page'),
]



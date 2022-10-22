from django.urls import path
from .views import *

app_name='books'
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('authors/',AuthorListView.as_view(),name='authors'),
    path('authors/<int:pk>/',AuthorDetailView.as_view(),name='author'),
    path('author/create/',AuthorCreateView.as_view(),name='author_create'),
    path('authors/edit/book/<int:pk>/',AuthorBooksEditView.as_view(),name='author_edit_book')
]


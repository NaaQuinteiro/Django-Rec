from django.urls import path
from .views import * 

urlpatterns = [
    path('livro/', LivroView.as_view(), name='Hello_world'),
    path('livro/<int:id>', LivroView.as_view(), name='Hello_world_by_id'),
    path('generoLivro/', GeneroLivroView.as_view(), name='genero_livro'),
    path('generoLivro/<int:id>', GeneroLivroView.as_view(), name='genero_livro_id'),
    path('genero/', GeneroView.as_view(), name='genero'),
    path('genero/<int:id>', GeneroView.as_view(), name='genero_id')
]
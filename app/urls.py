from django.urls import path
from .views import * 
from rest_framework.routers import DefaultRouter

# urls criadas automaticamente
router = DefaultRouter()

router.register(r'livro', LivroModelView)

router.register(r'genero', GeneroModelView)

router.register(r'generoLivro', GeneroLivroModelView)

urlpatterns= router.urls

# Urls criadas manualmente
# urlpatterns.append(path('livro/', LivroAPIView.as_view(), name='Hello_world'))
# urlpatterns.append(path('livro/<int:id>', LivroAPIView.as_view(), name='Hello_world_by_id'))
# urlpatterns.append(path('generoLivro/', GeneroLivroView.as_view(), name='genero_livro'))
# urlpatterns.append(path('generoLivro/<int:id>', GeneroLivroView.as_view(), name='genero_livro_id'))
# urlpatterns.append(path('genero/', GeneroView.as_view(), name='genero'))
# urlpatterns.append(path('genero/<int:id>', GeneroView.as_view(), name='genero_id'))
from rest_framework.serializers import ModelSerializer
from .models import *

# criação do serializer que retorna diversos valores do seu banco de dados, ele possui os metodos de create etc
class LivroSerializer(ModelSerializer):
    class Meta:
        #insira a qual dos seus models ele se refere 
        model = Livros
        #aui você diz que ele pode retornar varios livros ou salvar varios livros
        many = True
        #aqui ele retorna todas as colunas do seu banco 
        fields = '__all__'

class LivroSerializerTitulo(ModelSerializer):
    class Meta:
        #insira a qual dos seus models ele se refere 
        model = Livros
        #aui você diz que ele pode retornar varios livros ou salvar varios livros
        many = True
        #aqui ele retorna apenas as colunas especificadas
        fields = ('titulo',)   

class GeneroSerializer(ModelSerializer):   
    class Meta:
        #insira a qual dos seus models ele se refere 
        model = Genero
        #aui você diz que ele pode retornar varios livros ou salvar varios livros
        many = True
        #aqui ele retorna todas as colunas do seu banco 
        fields = '__all__'


class GeneroLivroSerializer(ModelSerializer):   
    class Meta:
        #insira a qual dos seus models ele se refere 
        model = GeneroLivro
        #aui você diz que ele pode retornar varios livros ou salvar varios livros
        many = True
        #aqui ele retorna todas as colunas do seu banco 
        fields = '__all__'


class GetGeneroLivroSerializer(ModelSerializer): 
    fk_livro = LivroSerializer(read_only = True) # aq é para ele pegar apenas livros que existem na tabela
    fk_genero =GeneroSerializer(read_only = True)
    class Meta:
        #insira a qual dos seus models ele se refere 
        model = GeneroLivro
        #aui você diz que ele pode retornar varios livros ou salvar varios livros
        many = True
        #aqui ele retorna todas as colunas do seu banco 
        fields = '__all__'

# o serializer é uma ponte entre o nosso back e o banco, ele nos ajuda muito 
         
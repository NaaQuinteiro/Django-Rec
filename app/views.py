from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import *
from .serializer import *
import json
# aba para criação de metodos = ao controler do projeto


#Modo automático - O ModelViewSet possui todos os metodos de crud
class LivroModelView(ModelViewSet):
    # tipo de querr para pegar tudo 
    queryset = Livros.objects.all()
    serializer_class = LivroSerializer
    # http_method_names = ('POST', 'GET')

class GeneroModelView(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    # http_method_names = ('POST', 'GET')

class GeneroLivroModelView(ModelViewSet):
    queryset = GeneroLivro.objects.all()
    serializer_class = GeneroLivroSerializer
    # http_method_names = ('POST', 'GET')

    def list (self, request, *args, **kwargs):
        # generoLivro = GeneroLivro.objects.select_related('fk_livro', 'fk_genero')
        generoLivro = GeneroLivro.objects.all()
        print(generoLivro.query)
        serializer = GetGeneroLivroSerializer(generoLivro, many=True)
        return Response(status=201, data=serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = GetGeneroLivroSerializer(instance, many=False)
        return Response(serializer.data)


# Modo manual
class LivroAPIView(APIView):
    #funções para chamar as classes, o request é do que ele está requisitando
    def get(self, request, id=''):

        if id:
            
            livros = Livros.objects.filter(id=id).first()

            if not livros:
                return Response(status=404, data={'mensagem': 'livro nao encontrado'})

            serializer = LivroSerializer(livros, many=False)
            return Response(status=200, data=serializer.data)
        else:

            livros = Livros.objects.all()
            serializer = LivroSerializer(livros, many=True)
            return Response(status=201, data=serializer.data)
        
    def post(self, request):
        #o body é o corpo da requisição
        # body = json.loads(request.body)
        #o loads ele converte bytes, strings e arrey de bytes para json (o documennto precisa estar em formato json)
        # serializer = LivroSerializer(body, many=False)
        body = request.data
        serializer = LivroSerializer(data=body, many=False)

        if not serializer.is_valid():
             return Response(status=400, data={'mensagem': 'dado ruim'})
        serializer.save()
        # print(serializer)

        return Response(status=201, data=serializer.data)
    
    def put(self, request, id):
        #verificando que o livro existe no banco de dados
        #aqui estamos tentando encontrar um livro no bancos de dados com o ID fornecido  
        livro = Livros.objects.filter(id=id).first()
        if not livro:
            #se nenhum livro for encontrado ele retornara um erro 404
            return Response(status=404, data={'mensagem': 'livro nao encontrado'})
        
        serializer = LivroSerializer(livro, data=request.data)
        if not serializer.is_valid():
            return Response(status=400, data={'mensagem': 'dados invalidos'})
        
        serializer.save()
        return Response(status=200, data=serializer.data)
    
    def delete(self,request, id):
        livro = Livros.objects.filter(id=id).first()
        if not livro:
            #se nenhum livro for encontrado ele retornara um erro 404
            return Response(status=404, data={'mensagem': 'livro nao encontrado'})
        livro.delete()
        return Response(status=204,data={'mensagem': 'deletou cachorreira'})

   
class GeneroView(APIView):
    
    def get(self, request, id=''):

        if id:
            
            genero = Genero.objects.filter(id=id).first()

            if not genero:
                return Response(status=404, data={'mensagem': 'genero nao encontrado'})

            serializer = GeneroSerializer(genero, many=False)
            return Response(status=200, data=serializer.data)
        else:

            genero = Genero.objects.all()
            serializer = GeneroSerializer(genero, many=True)
            return Response(status=201, data=serializer.data)
        

    def post(self, request):
        #o body é o corpo da requisição
        # body = json.loads(request.body)
        #o loads ele converte bytes, strings e arrey de bytes para json (o documennto precisa estar em formato json)
        # serializer = LivroSerializer(body, many=False)
        body = request.data
        serializer = GeneroSerializer(data=body, many=False)

        if not serializer.is_valid():
             return Response(status=400, data={'mensagem': 'dado ruim'})
        serializer.save()
        # print(serializer)
        return Response(status=201, data=serializer.data)
        

class GeneroLivroView(APIView):
    def get(self, request, id=''):
        # generoLivro = GeneroLivro.objects.select_related('fk_livro', 'fk_genero')
        generoLivro = GeneroLivro.objects.all()
        print(generoLivro.query)
        serializer = GetGeneroLivroSerializer(generoLivro, many=True)
        return Response(status=201, data=serializer.data)
    
    
    def post(self, request):
        #o body é o corpo da requisição
        # body = json.loads(request.body)
        #o loads ele converte bytes, strings e arrey de bytes para json (o documennto precisa estar em formato json)
        # serializer = LivroSerializer(body, many=False)
        body = request.data
        serializer = GeneroLivroSerializer(data=body, many=False)
        if not serializer.is_valid():
             return Response(status=400, data={'mensagem': 'dado ruim'})
        serializer.save()
        # print(serializer)
        return Response(status=201, data=serializer.data)
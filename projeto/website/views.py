from django.shortcuts import render
#from .models import Pessoa

# Create your views here.
def home(request):
    return render(request, 'index.html')

def contato(request):
    nome = 'MATHEUS'
    line = '50'
    return render(request, 'proxpag.html',{'nome': nome,'line': line})

def dieta(request):
    return render(request, 'dieta.html')


#def lista_pessoas(request):
   # pessoas = Pessoa.objects.all().order_by('nome')
#    return render(request, 'pessoas.html', {'pessoas': pessoas})
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def contato(request):
    nome = 'MATHEUS'
    line = '50'
    return render(request, 'proxpag.html',{'nome': nome,'line': line})
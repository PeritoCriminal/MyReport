from django.shortcuts import render

def index(request):
    aviso = 'Próximo pásso desse projeto: Determinar as variáveis globias, como são impelmentadas, não esquecer de incluir o diretor'
    importante = 'Não posso esquecer que tenho outras entregas.'
    context = {
        'aviso': aviso,
        'recado': importante,
    }
    return render(request, 'index.html', context)

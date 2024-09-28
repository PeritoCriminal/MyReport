"""

Copyright (c) 2024 Marcos de Oliveira Capristo
Todos os direitos reservados.

MYREPORT é um projeto independente.
Oferece um ambiente para edição de laudos periciais,
voltado especialmente para Peritos Criminais Oficiais do Estado de São Paulo.
Idealizado e inicialmente desenvolvido pelo Perito Criminal Marcos de Oliveira Capristo.
Contato: marcos.moc@policiacientifica.sp.gov.br | (19) 9 8231-2774


"""

"""

VIEW INDEX, A DESENVOLVER


"""



from django.shortcuts import render

def index(request):
    aviso = 'Próximo pásso desse projeto: Determinar as variáveis globias, como são impelmentadas, não esquecer de incluir o diretor'
    importante = 'Não posso esquecer que tenho outras entregas.'
    context = {
        'aviso': aviso,
        'recado': importante,
    }
    return render(request, 'index.html', context)

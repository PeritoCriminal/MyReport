from django.shortcuts import render

context = {
    'sobre': 'Laudo Téncio Pericial',
}

def HeaderImportView(request):
    return render(request, 'headerreport.html', context)
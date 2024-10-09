from django.shortcuts import render

def contenidoDinamico(request):
    categorias = ['HTML', 'CSS', 'JavaScript','SQL','Python','Django']
    context = {'categorias': categorias}
    return render(request, 'rutasDinamicas.html', context)
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import LaboratorioForm
from .models import Laboratorio


class LaboratorioListView(ListView):
    """ Clase para mostrar el listado
        completo de los laboratorios """
    model = Laboratorio  # nombre del modelo donde se realiza el queryset
    template_name = "laboratorio/index.html"  # template a utilizar
    context_object_name = 'laboratorios'  # nombre otorgado a los objetos


def agregar(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = LaboratorioForm()

    return render(request, 'laboratorio/agregar.html', {'form': form})


def editar(request, id):
    """ Función para editar los laboratorios
        laboratorio = El objeto a editar
        LaboratorioForm = clase de formulario
        form = Instancia de la clase LaboratorioForm"""
    laboratorio = Laboratorio.objects.get(id=id)

    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = LaboratorioForm(instance=laboratorio)

    return render(request, 'laboratorio/editar.html', {'form': form})

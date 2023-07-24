from django.urls import path
from .views import LaboratorioListView, agregar, editar

urlpatterns = [
    path('', LaboratorioListView.as_view(), name='index'),
    path('agregar/', agregar, name='agregar'),
    path('editar/<int:id>', editar, name='editar'),
]
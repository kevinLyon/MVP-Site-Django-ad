from django.shortcuts import render
from django.http import HttpResponse

from .models import Categoria
from.models import Anuncio


def home(request):
    categoria = Categoria.objects.all()
    ultimos_anuncios = Anuncio.objects.all()[:12]

    return render(request, 'index.html', {'categorias': categoria, 'anuncios': ultimos_anuncios})

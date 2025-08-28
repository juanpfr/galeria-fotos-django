from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Photo

# Create your views here.

def home(request):
    photos = Photo.objects.all()
    return render(request, 'galeria/home.html', {'photos': photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'galeria/photo_detail.html', {'photo': photo})

def photo_search(request):
    query = request.GET.get('q')
    resultados = []
    if query:
        resultados = Photo.objects.filter(title__icontains=query)

    context = {
        'query': query,
        'resultados': resultados,
    }
    
    return render(request, 'galeria/photo_search.html', context)
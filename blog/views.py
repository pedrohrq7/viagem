from django.shortcuts import render
from rest_framework import viewsets
from blog.serializers import TopicoSerializer
from blog.models import Topico

# Create your views here.
def blog(request):
    contexto = {
        'titulo' : 'Jornada Viagem | Blog'
    }
    return render(request, 
                  'blog/index.html',
                  contexto,
                  )


# Create your views here.
class TopicoViewSet(viewsets.ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer
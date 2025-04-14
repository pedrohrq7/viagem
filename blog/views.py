from django.shortcuts import render

# Create your views here.
def blog(request):
    contexto = {
        'titulo' : 'Jornada Viagem | Blog'
    }
    return render(request, 
                  'blog/index.html',
                  contexto,
                  )
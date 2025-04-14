
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('cadastro/', include('cadastro.urls')),
    path('destinos/', include('destinos.urls')),
    path('fotos/', include('fotos.urls')),
    path('blog/', include('blog.urls')),
]

urlpatterns +=[
    path('accounts/', include('django.contrib.auth.urls')),
]


"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from designation.models import Designacoe

api = NinjaAPI()

@api.get("/search")
def search(request, nome: str):
    try:
        result = Designacoe.objects.get(unidade=nome)
        return {'designacao' : result.designacao}
    except Designacoe.DoesNotExist:
        return {'erro' : "Designacao nao localizada"}

@api.post("/create")
def create(request):
    unidade = request.POST.get('unidade')
    designacao = request.POST.get('designacao')
    try:
        retorno = Designacoe.objects.get(unidade=unidade)
        return {'erro' : "Designacao ja existente", 'unidade' : retorno.unidade,'designacao' : retorno.designacao}
    except Designacoe.DoesNotExist:
        Designacoe.objects.create(unidade=unidade, designacao=designacao)
        return {'sucesso' : "Designacao criada",'unidade' : unidade, 'designacao' : designacao}
    except Exception as e:
        return {'erro' : "Designacao nao criada", 'exception' : e}

    
urlpatterns = [
    path(r'jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', include('designation.urls'), name='home_url'),
    path('api/',api.urls), # Django API URLs
]

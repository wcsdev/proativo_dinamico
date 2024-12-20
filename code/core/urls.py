from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI, Schema
from django.http import JsonResponse
from designation.models import Designacoe

# Inicialização da API
api = NinjaAPI()

# Definindo o modelo Pydantic para validação da requisição POST
class CreateDesignacaoRequest(Schema):
    unidade: str
    designacao: str

# Endpoint GET - Pesquisa de Designação
@api.get("/search")
def search(request, nome: str):
    try:
        # Buscar a designação pela unidade
        result = Designacoe.objects.get(unidade=nome)
        return {'designacao': result.designacao}
    except Designacoe.DoesNotExist:
        return JsonResponse({'detail': f"Designacao nao encontrada para a unidade '{nome}'"}, status=404)

# Endpoint POST - Criar uma nova designação
@api.post("/create")
def create(request, data: CreateDesignacaoRequest):
    unidade = data.unidade
    designacao = data.designacao

    # Verificar se os campos obrigatórios foram informados
    if not unidade:
        return JsonResponse({'detail': "Campo 'unidade' nao informado"}, status=400)
    if not designacao:
        return JsonResponse({'detail': "Campo 'designacao' nao informado"}, status=400)

    try:
        # Verificar se a unidade já existe
        consulta = Designacoe.objects.filter(unidade=unidade).first()
        if consulta:
            return JsonResponse({'detail': f"Designacao ja existente para a unidade '{unidade}'"}, status=409)
        
        # Criar uma nova designação
        Designacoe.objects.create(unidade=unidade, designacao=designacao)
        return JsonResponse({'sucesso': "Designacao criada", 'unidade': unidade, 'designacao': designacao}, status=201)
    
    except Exception as e:
        return JsonResponse({'detail': f"Erro ao criar designacao: {str(e)}"}, status=500)

# Definindo as URLs do projeto
urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', include('designation.urls'), name='home_url'),
    path('api/', api.urls),  # Django API URLs
]

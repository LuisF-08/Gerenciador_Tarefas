from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views  

# --- CONFIGURAÇÃO DA API (ROUTER) ---
# O Router cria automaticamente as URLs para o seu ViewSet
router = DefaultRouter()
router.register(r'lista', views.TarefaViewSet, basename='tarefa')
# Isso vai gerar URLs como: GET /tasks/api/lista/

urlpatterns = [
    # --- PÁGINAS PRINCIPAIS (HTML) ---
    path('', views.painel, name='painel'),
    path('sobre/', views.sobre, name='about'),
    path('erro/', views.erro, name='error'),
    
    # --- BUSCA (HTML) ---
    path('buscar/', views.pagina_busca, name='pagina_busca'), 
    path('buscar/resultado/', views.resultado_busca, name='resultado_busca'),
    path('buscar/<int:task_id>/', views.buscar_task, name='buscar_task'),

    # --- AÇÕES CRUD (HTML) ---
    path('adicionar/', views.adicionar_task, name='adicionar_task'), 
    path('atualizar/<int:task_id>/', views.atualizar_task, name='atualizar_task'),
    path('deletar/<int:task_id>/', views.deletar_task, name='deletar_task'),
    path('marcar_estado/<int:task_id>/<str:novo_estado>/', views.marcar_estado, name='marcar_estado'),
    
    # --- ROTAS DA API (JWT + VIEWSET) ---
    
    # 1. Rotas automáticas do ViewSet (CRUD via JSON)
    # Acessível em: http://127.0.0.1:8000/tasks/api/lista/
    path('api/', include(router.urls)), 
    
    # 2. Rota para pegar o Token (Login da API)
    # Acessível em: http://127.0.0.1:8000/tasks/api/token/
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # 3. Rota para renovar o Token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
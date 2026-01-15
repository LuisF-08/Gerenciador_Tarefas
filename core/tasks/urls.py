from django.urls import path
from . import views  

urlpatterns = [
    # --- PÁGINAS PRINCIPAIS ---
    path('', views.painel, name='painel'),
    path('sobre/', views.sobre, name='about'),
    path('erro/', views.erro, name='error'),
    
    # --- BUSCA ---
    path('buscar/', views.pagina_busca, name='pagina_busca'), 
    path('buscar/resultado/', views.resultado_busca, name='resultado_busca'),
    path('buscar/<int:task_id>/', views.buscar_task, name='buscar_task'),

    # --- AÇÕES (CRUD) ---
    path('adicionar/', views.adicionar_task, name='adicionar_task'), 
    path('atualizar/<int:task_id>/', views.atualizar_task, name='atualizar_task'),
    path('deletar/<int:task_id>/', views.deletar_task, name='deletar_task'),
    path('marcar_estado/<int:task_id>/<str:novo_estado>/', views.marcar_estado, name='marcar_estado'),
]
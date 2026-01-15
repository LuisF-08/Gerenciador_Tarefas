from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from django.db.models import Q
from .models import Task

# --- VIEWS DE NAVEGAÇÃO E LEITURA ---

def painel(request):
    tasks = Task.objects.all().order_by('-id')
    tarefa_antiga = Task.objects.order_by('id').first()

    tarefas_contexto = {
        'tasks' : tasks,
        'tarefa_antiga': tarefa_antiga 
    }
    return render(request, 'index.html', tarefas_contexto)

def sobre(request):
    return render(request, 'about.html')

def erro(request):
    return render(request, 'error.html')

# --- VIEWS DE BUSCA ---

def pagina_busca(request):
    return render(request, 'busca_form.html')

# 2. Processa a busca (Lógica ID ou Título)
def resultado_busca(request):
    query = request.GET.get('q') # Pega o que foi digitado
    resultados = []

    if query:
        # Se for número, busca ID exato OU título contém o número
        if query.isdigit():
            resultados = Task.objects.filter(
                Q(id=query) | Q(titulo__icontains=query)
            )
        # Se for texto, busca só no título
        else:
            resultados = Task.objects.filter(titulo__icontains=query)
            
    return render(request, 'busca_resultado.html', {'resultados': resultados, 'termo_buscado': query})

# 3. Visualização direta (caso clique em "Detalhes" num resultado)
def buscar_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'buscar_tarefa.html', {'task': task})

# --- VIEWS DE AÇÃO (CRUD) ---

def adicionar_task(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao', '')
        estado = request.POST.get('estado', 'pendente') 
        Task.objects.create(titulo=titulo, descricao=descricao, estado=estado)
        
        messages.success(request, 'Tarefa adicionada com sucesso!')
    else:
            messages.error(request, 'Erro ao adicionar Tarefa.')
        
    return redirect('painel')

def atualizar_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.titulo = request.POST.get('titulo', task.titulo)
        task.descricao = request.POST.get('descricao', task.descricao)
        task.save()
        
        messages.success(request, 'Tarefa Atualizada com sucesso!')
        return redirect('painel')
    
    return render(request, 'editar_form.html', {'task': task})

def deletar_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        messages.success(request, 'Tarefa Deletada com sucesso!')
    else:
            messages.error(request, 'Erro ao deletar.')    
    
    return redirect('painel')

def marcar_estado(request, task_id, novo_estado):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        if novo_estado in dict(Task.STATUS_CHOICES).keys():
            task.estado = novo_estado
            task.save()
            messages.success(request, f'Tarefa marcada como {novo_estado} com sucesso!')
        else:
            messages.error(request, 'Estado inválido fornecido.')
            
    return redirect('painel')
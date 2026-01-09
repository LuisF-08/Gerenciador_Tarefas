from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from .models import Task

# --- VIEWS DE NAVEGAÇÃO E LEITURA ---

def painel(request):
    tasks = Task.objects.all().order_by('-id')
    tarefas_contexto = {
        'tasks' : tasks
    }
    return render(request, 'index.html', tarefas_contexto)

def sobre(request):
    return render(request, 'about.html')

def erro(request):
    return render(request, 'error.html')

# --- VIEWS DE BUSCA ---

def pagina_busca(request):
    # Se enviou o formulário com o ID
    if request.method == 'POST':
        id_buscado = request.POST.get('id_para_buscar')
        # Redireciona para a URL que exibe o resultado
        return redirect('buscar_task', task_id=id_buscado)
    
    # Se apenas acessou a página
    return render(request, 'busca_form.html')

def buscar_task(request, task_id):
    try:
        # Tenta pegar a tarefa pelo ID
        task = Task.objects.get(id=task_id)
        return render(request, 'busca_resultado.html', {'task': task})
    
    except Task.DoesNotExist:
        # Se não existir, joga para a sua view de erro personalizada
        return redirect('erro')

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
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.titulo = request.POST.get('titulo', task.titulo)
        task.descricao = request.POST.get('descricao', task.descricao)
        task.estado = request.POST.get('estado', task.estado)
        task.save()
        
        messages.success(request, 'Tarefa Atualizada com sucesso!')
    else:
            messages.error(request, 'Erro na atualização.')
        
    return redirect('painel')

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
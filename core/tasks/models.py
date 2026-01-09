from django.db import models

class Task(models.Model):
    
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('concluido', 'Concluído'),
        ('erro', 'Erro'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True,
                                null=True)
    estado = models.CharField(max_length=20,
                            choices=STATUS_CHOICES,
                            default='pendente')
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.titulo} - {self.estado} - {self.data_criacao.strftime('%Y-%m-%d %H:%M:%S')}"
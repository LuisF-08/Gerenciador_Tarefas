# 📝 Django Task Manager (Gerenciador de Tarefas)

Um sistema web completo e moderno para gerenciamento de tarefas diárias, desenvolvido com **Python/Django** e estilizado com **Bootstrap 5,CSS3 e JavaScript**. O projeto foca em uma interface limpa, responsiva e com interações de usuário fluidas (CRUD Completo).

---

## 🚀 Funcionalidades

O sistema possui as seguintes capacidades:

*   **Painel de Controle (Dashboard):** Visualização de todas as tarefas em formato de *Cards* modernos.
*   **Adicionar Tarefa:** Criação rápida via **Modal** (Pop-up) sem sair da página principal.
*   **Listagem Inteligente:**
    *   Diferenciação visual entre tarefas **Pendentes** (Amarelo) e **Concluídas** (Verde).
    *   Efeitos de *Hover* (sombra e elevação) nos cartões.
*   **Edição Completa:** Página dedicada para edição com formulários estilizados (*Floating Labels*).
*   **Gestão de Status:** Botão rápido para marcar tarefas como Concluídas.
*   **Exclusão Segura:** Botão de deletar com confirmação e proteção via método POST.
*   **Busca por ID:** Sistema para localizar tarefas específicas pelo seu identificador.

---

## 🛠️ Tecnologias Utilizadas

*   **Backend:** Python 3.11+, Django 5.x
*   **Frontend:** HTML5,Javascript, CSS3, Bootstrap 5.3 (incluindo Bootstrap Icons)
*   **Banco de Dados:** PostgreSQL (Configurado) / SQLite (Padrão Django)
*   **Estilização:** CSS Customizado para gradientes, sombras e animações.
*   **Versionamento:** Git.

---

## 📂 Estrutura do Projeto em MTV(Model-Template-View)

A estrutura principal do código foi organizada da seguinte forma:

```text
Django_Lista/
│
├── .env                     # Variáveis de ambiente (Senhas, Chaves secretas)
├── requirements.txt         # Lista de dependências para instalação (pip)
├── README.md                # Documentação do projeto
│
└── core/                    # Raiz do Projeto Django
    ├── manage.py            # Utilitário de comando do Django
    │
    ├── core/                # Configurações Globais do Projeto
    │   ├── settings.py      # Configuração de Banco de Dados, Apps e Middleware
    │   └── urls.py          # Rotas principais (Redirecionam para os apps)
    │
    └── tasks/               # Aplicação Principal (Gerenciador de Tarefas)
        ├── models.py        # Estrutura das Tabelas do Banco de Dados
        ├── views.py         # Lógica do CRUD (Criar, Ler, Atualizar, Deletar)
        ├── urls.py          # Rotas específicas das tarefas
        │
        └── templates/       # Arquivos HTML (Frontend)
            ├── base.html            # Layout mestre (Navbar e Rodapé)
            ├── index.html           # Tela principal (Lista e Modal de criar)
            ├── editar_form.html     # Formulário de edição estilizado
            ├── busca_resultado.html # Tela de resultados da pesquisa
            └── ...                  # Outras páginas auxiliares
```

---

## 🔧 Como Executar o Projeto

Siga os passos abaixo para rodar o projeto em sua máquina local:

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/django-task-manager.git
cd Django_Lista
```

### 2. Crie e ative um ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install django psycopg2  # (Adicione outros pacotes se necessário)
```

### 4. Configure o Banco de Dados
Certifique-se de que o PostgreSQL está rodando e as credenciais no `settings.py` estão corretas (ou use o SQLite padrão).

### 5. Execute as Migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Inicie o Servidor
```bash
python manage.py runserver
```

Acesse em seu navegador: `http://127.0.0.1:8000/`

---

## 🎨 Destaques de Design (UI/UX)

O projeto conta com classes personalizadas para melhorar a experiência do usuário:

*   **`task-card`**: Cartões com borda colorida dinâmica baseada no status da tarefa.
*   **`btn-hover-effect`**: Botões que aumentam levemente de tamanho ao passar o mouse.
*   **`page-wrapper`**: Fundo com gradiente suave na página de edição.
*   **Interatividade**: Botões de ação (Editar, Excluir, Concluir) com ícones intuitivos.

---

## 🔐 Segurança

*   Uso de **CSRF Tokens** em todos os formulários (POST).
*   Rotas de exclusão e alteração de estado protegidas (não acessíveis via GET direto na URL para ações destrutivas).
*   Tratamento de erros `404` (Get Object or 404) caso a tarefa não exista.

---

## 👤 Autor

Desenvolvido por **Luis** durante estudos de Django e Desenvolvimento Web Fullstack.
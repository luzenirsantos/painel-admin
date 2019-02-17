from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from mysite.models import Funcionario
from loja.forms import InsereFuncionarioForm
from mysite.models import Cliente
from loja.forms import InsereClienteForm


# PÁGINA PRINCIPAL
# ----------------------------------------------

class IndexTemplateView(TemplateView):
    template_name = "loja/index.html"


# LISTA DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioListView(ListView):
    template_name = "loja/lista_fun.html"
    model = Funcionario
    context_object_name = "funcionarios"


# CADASTRAMENTO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioCreateView(CreateView):
    template_name = "loja/cria_fun.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("loja:lista_funcionarios")


# ATUALIZAÇÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioUpdateView(UpdateView):
    template_name = "loja/atualiza_fun.html"
    model = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'
    success_url = reverse_lazy("loja:lista_funcionarios")


# EXCLUSÃO DE FUNCIONÁRIOS
# ----------------------------------------------

class FuncionarioDeleteView(DeleteView):
    template_name = "loja/exclui_fun.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("loja:lista_funcionarios")


# LISTA DE CLIENTES
# ----------------------------------------------

class ClienteListView(ListView):
    template_name = "loja/lista_cli.html"
    model = Cliente
    context_object_name = "clientes"


# CADASTRAMENTO DE CLIENTES
# ----------------------------------------------

class ClienteCreateView(CreateView):
    template_name = "loja/cria_cli.html"
    model = Cliente
    form_class = InsereClienteForm
    success_url = reverse_lazy("loja:lista_clientes")


# ATUALIZAÇÃO DE CLIENTES
# ----------------------------------------------

class ClienteUpdateView(UpdateView):
    template_name = "loja/atualiza_cli.html"
    model = Cliente
    fields = '__all__'
    context_object_name = 'cliente'
    success_url = reverse_lazy("loja:lista_clientes")


# EXCLUSÃO DE CLIENTES
# ----------------------------------------------

class ClienteDeleteView(DeleteView):
    template_name = "loja/exclui_cli.html"
    model = Cliente
    context_object_name = 'cliente'
    success_url = reverse_lazy("loja:lista_clientes")


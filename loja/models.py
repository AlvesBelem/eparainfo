from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    id_sessao = models.CharField(max_length=200, null=True, blank=True)
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Nome: {self.nome} | Email: {self.email}"
    
class Cor(models.Model):
    id_cor = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    codigo = models.CharField(max_length=100, null=True, blank=True)
    id_detalhe = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"Nome: {self.nome} | Codigo: {self.codigo}"
    
class Marca(models.Model):
    id_marca = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    id_produto = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"Nome: {self.nome}"
    
class Mram(models.Model):
    id_mram = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    id_produto = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"Nome: {self.tipo}"
    
class Armazenamento(models.Model):
    id_hd = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    id_produto = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"Nome: {self.tipo}"
    
class Processador(models.Model):
    id_process = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    id_produto = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"Nome: {self.tipo}"
    

class Categoria(models.Model): 
    id_categoria = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    id_produto = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.nome)
    
class Tipo(models.Model):
    id_categoria = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    id_produto = models.CharField(max_length=200, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return str(self.nome)
    
class Grafic(models.Model): 
    id_grafic = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    id_produto = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.nome)
    
class TipoTela(models.Model): 
    id_tipoTela = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    id_produto = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.nome)

class So(models.Model): 
    id_so = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    id_produto = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.nome)
    
class Modelo(models.Model): 
    id_modelo = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    id_produto = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.nome)
    
# class Dimensao(models.Model):
#     Altura = models.DecimalField(max_digits=5, decimal_places=2)
#     Largura = models.DecimalField(max_digits=5, decimal_places=2)
#     Comprimento = models.DecimalField(max_digits=5, decimal_places=2)
#     id_produto = models.CharField(max_length=200, null=True, blank=True)
    
#     def __str__(self):
#         return str(self.nome)
    
class Produto(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.TextField(max_length=1000,null=True, blank=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    tipo = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.SET_NULL)
    marca = models.ForeignKey(Marca, null=True, blank=True, on_delete=models.SET_NULL)
    memoria_ram = models.ForeignKey(Mram, null=True, blank=True, on_delete=models.SET_NULL)
    armazenamento = models.ForeignKey(Armazenamento, null=True, blank=True, on_delete=models.SET_NULL)
    processador = models.ForeignKey(Processador, null=True, blank=True, on_delete=models.SET_NULL)
    grafic = models.ForeignKey(Grafic, null=True, blank=True, on_delete=models.SET_NULL)
    tipoTela = models.ForeignKey(TipoTela, null=True, blank=True, on_delete=models.SET_NULL)
    so = models.ForeignKey(So, null=True, blank=True, on_delete=models.SET_NULL)
    modelo = models.ForeignKey(Modelo, null=True, blank=True, on_delete=models.SET_NULL)
    ativo = models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"Nome: {self.nome} | Categoria: {self.categoria} | Tipo: {self.tipo} | Preço: {self.preco}"
    
    def total_vendas(self):
        itens = ItensPedido.objects.filter(pedido__finalizado=True, item_estoque__produto=self.id)
        total = sum([item.quantidade for item in itens])
        return total
    
class ItemEstoque(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.SET_NULL)
    preco_sugerido = models.DecimalField(max_digits=10, decimal_places=2, default=0.000)
    preco_praticado = models.DecimalField(max_digits=10, decimal_places=2, default=0.000)
    cor = models.ForeignKey(Cor, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)
    altura = models.CharField(max_length=200, null=True, blank=True)
    largura = models.CharField(max_length=200, null=True, blank=True)
    comprimento = models.CharField(max_length=200, null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True, default=0.000)
    ativo = models.BooleanField(default=True)
    oferta = models.BooleanField(default=False)
    ofertaDia = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Nome: {self.produto.nome} | Cor: {self.cor.nome} | Tamanho: {self.tamanho}"
    


class ImageItemEstoque(models.Model):
    item_estoque = models.ForeignKey(ItemEstoque, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='imagens/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Image uploaded at {self.uploaded_at}"
    

class Endereco(models.Model):
    rua = models.CharField(max_length=400, null=True, blank=True)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    cep = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=200, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"Email: {self.cliente.nome} | Rua: {self.rua} | CEP: {self.cep} | Cidade: {self.cidade}"
    
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    data_finalizacao = models.DateTimeField(null=True, blank=True,)
    finalizado = models.BooleanField(default=False)
    codigo_transacao = models.CharField(max_length=100, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"Cliente: {self.cliente.nome} | Número: {self.id} | Finalizado: {self.finalizado}"
    
    @property
    def quantidade_total(self):
        itens_pedido = ItensPedido.objects.filter(pedido__id=self.id)
        quantidade = sum(
            [item.quantidade for item in itens_pedido]
        )
        return quantidade
    
    @property
    def preco_total(self):
        itens_pedido = ItensPedido.objects.filter(pedido__id=self.id)
        preco = sum(
            [item.preco_total for item in itens_pedido]
        )
        return preco
    
    @property
    def itens(self):
        itens_pedido = ItensPedido.objects.filter(pedido__id=self.id)
        return itens_pedido
    
    
class ItensPedido(models.Model):
    item_estoque = models.ForeignKey(ItemEstoque, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f"Pedido: {self.pedido.id} | Produto: {self.item_estoque.produto.nome} | Tamanho: {self.item_estoque.tamanho} | Cor: {self.item_estoque.cor.nome} | Qtd: {self.quantidade}"
    
    @property
    def preco_total(self):
        return self.quantidade * self.item_estoque.produto.preco
    
class BannerGrid(models.Model):
    nome = models.CharField(max_length=400, null=True, blank=True)
    imagem = models.ImageField(upload_to='bannerG/')
    link_destino = models.CharField(max_length=400, null=True, blank=True)
    ativo = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Nome: {self.nome} | link_destino: {self.link_destino} | Ativo: {self.ativo}"
    
class BannerPrincipal(models.Model):
    nome = models.CharField(max_length=400, null=True, blank=True)
    imagem_web = models.ImageField(upload_to='bannerPW/')
    imagem_mobile = models.ImageField(upload_to='bannerPM/')
    link_destino = models.CharField(max_length=400, null=True, blank=True)
    ativo = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Nome: {self.nome} | link_destino: {self.link_destino} | Ativo: {self.ativo}"
    
class BannerIndividual(models.Model):
    nome = models.CharField(max_length=400, null=True, blank=True)
    imagem_web = models.ImageField(upload_to='bannerIW/')
    imagem_mobile = models.ImageField(upload_to='bannerIM/')
    link_destino = models.CharField(max_length=400, null=True, blank=True)
    ativo = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Nome: {self.nome} | link_destino: {self.link_destino} | Ativo: {self.ativo}"
    
class Pagamento(models.Model):
    id_pagamento = models.CharField(max_length=400)
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL)
    aprovado = models.BooleanField(default=False)
    
    

    
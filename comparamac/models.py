from django.db import models

class Cor(models.Model):
    COR_CHOICES = [
        ('B', 'Azul Estelar'),
        ('G', 'Cinza Espacial'),
        ('S', 'Prata'),
        ('M', 'Meia Noite'),
        ('R', 'Ouro Rosa')
    ]
    
    nome = models.CharField(max_length=1, choices=COR_CHOICES, unique=True)

    def __str__(self):
        return dict(self.COR_CHOICES).get(self.nome, self.nome)

class Notebook(models.Model):
    CATEGORIA_CHOICES = [
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    ]

    # Categoria
    categoria = models.CharField(max_length=1, choices=CATEGORIA_CHOICES, blank=True, null=True)

    # Identificação
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)
    nome = models.CharField(max_length=100)
    cores = models.ManyToManyField(Cor)
    id_do_modelo = models.CharField(max_length=50, unique=True)
    modelo = models.CharField(max_length=10)
    emc = models.CharField(max_length=10, blank=True, null=True)

    # Processamento
    cpu = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    armazenamento = models.CharField(max_length=50)

    # Tela
    tamanho = models.DecimalField(max_digits=4, decimal_places=1)
    resolucao = models.CharField(max_length=50)
    tipo_tela = models.CharField(max_length=50)
    true_tone = models.CharField(max_length=50)
    suporte_a_telas = models.CharField(max_length=50)

    # Bateria
    autonomia = models.CharField(max_length=50)
    carregador = models.CharField(max_length=50)
    conexao_bateria = models.CharField(max_length=50)

    # Dimensões
    espessura = models.DecimalField(max_digits=5, decimal_places=2)
    largura = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)

    # Áudio
    tipo_audio = models.CharField(max_length=200)

    # Conectividade
    wifi = models.CharField(max_length=50)
    bluetooth = models.CharField(max_length=50)
    usb = models.CharField(max_length=50)
    hdmi = models.CharField(max_length=50)
    entrada_fone = models.CharField(max_length=50)
    microfone = models.CharField(max_length=50)

    # Câmera
    resolucao_camera = models.CharField(max_length=50, blank=True, null=True)

    # Software
    sistema_operacional = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

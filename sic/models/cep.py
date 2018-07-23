from django.db import models

#===============================================================================================
class Pais(models.Model):
    codigo      = models.CharField('Código', max_length=5)
    nome        = models.CharField('Nome', max_length=30)
    nomeFormal  = models.CharField('Nome formal', max_length=50)
    fone        = models.CharField(max_length=5, null=True, blank=True)
    sigla       = models.CharField(max_length=4, null=True, blank=True)
    sigla2      = models.CharField(max_length=4, null=True, blank=True)
    criado_em   = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    atualizado_em = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self): return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Paises'
        db_table = 'paises'


#===============================================================================================
class Estado(models.Model):

    nome = models.CharField(max_length=30, unique=True)
    pais_id = models.ForeignKey('Pais', on_delete=models.CASCADE)
    sigla = models.CharField(max_length=5, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modificado_em = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self): return self.nome

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        db_table = 'estados'


#===============================================================================================
class Municipio(models.Model):

    nome = models.CharField(max_length=30)
    estado_id = models.ForeignKey('Estado', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modificado_em = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self): return self.nome

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        db_table = 'municipios'


#===============================================================================================
class Cidade(models.Model):

    nome = models.CharField(max_length=30)
    municipio_id = models.ForeignKey('Municipio', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modificado_em = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self): return self.nome

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        db_table = 'cidades'


#===============================================================================================
class Bairro(models.Model):

    nome = models.CharField(max_length=30)
    cidade_id = models.ForeignKey('Cidade', on_delete=models.CASCADE, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    modificado_em = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self): return self.nome

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'
        db_table = 'bairros'

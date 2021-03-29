from django.db import models
from django.db.models.fields import CharField, IntegerField

class Produto(models.Model):
    nome = models.CharField('Nome: ', max_length=100)
    preco = models.DecimalField('Preço: ', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em estoque: ')

    '''função str que apresenta nosso objetio instânciado de acordo como queremos = quando apresentar o objeto
    apresenta pelo nome dele ''' 
    
    def __str__(self):
        return self.nome   


class Cliente(models.Model):
    nome = models.CharField('Nome: ', max_length=100)
    sobrenome = models.CharField('Sobrenome: ', max_length=100)
    email = models.EmailField('Email: ', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'



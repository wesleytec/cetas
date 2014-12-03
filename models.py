# CADASTRO DE FAUNA COLEÇÃO
from django.db import models


CLASSE_CHOICE = (
	('1', 'AMPHIBIA'),
	('2', 'REPTILIA'),
	
)

ORDEM_CHOICE = (
	('1', 'ANURA'),
	('2', 'GYMNOPHIONA'),
	('3', 'CROCODYLIA'),
	('4', 'SQUAMATA'),
	('5', 'TESTUDINES'),
)

SUB_ORDEM_CHOICE = (
	('1', '----'),
	('2', 'AMPHISBAENIA'),
  ('3', 'OPHIDIA'),
	('4', 'SAURIA'),
)

FAMILIA_CHOICE = (
	('1', 'Bufonidae'),
	('2', '...'),
	('3', '...'),
	('4', '...'),
)

IDENTIFICA_CHOICE = (
	('1', 'Rhinella crucifer (Wied-Neuwied,1821)'),
	('2', '...'),
	('3', '...'),
	('4', '...'),
)

NOME_COMUM_CHOICE = (
	('1', 'Sapo cucuru'),
	('2', '...'),
	('3', '...'),
	('4', '...'),
)


AMBIENTE_CHOICE = (
	('1', 'Caatinga'),
	('2', 'Cerrado'),
	('3', 'Area de transicao'),
	('4', 'Area habitada'),
)

AREA_CHOICE = (
	('1', 'Direta'),
	('2', 'Indireta'),
)



class Registro(models.Model):
	classe = models.CharField(max_length=1, choices=CLASSE_CHOICE)
  ordem = models.CharField(max_length=1, choices=ORDEM_CHOICE)
  subordem = models.CharField(max_length=1, choices=SUB_ORDEM_CHOICE)
	familia = models.CharField(max_length=1, choices=FAMILIA_CHOICE)
  identificacao = models.CharField('Nome Cientifico / Autor',max_length=1, choices=IDENTIFICA_CHOICE)
  nome = models.CharField('Nome Comum',max_length=1, choices=NOME_COMUM_CHOICE)
	Data = models.DateTimeField()
	coletor = models.CharField(max_length=100)
	latitude = models.IntegerField('Latitude',max_length=50)
  longitude = models.IntegerField('Longitude',max_length=50)
	coleta = models.CharField('Local de Coleta',max_length=100)
	municipio = models.CharField('Municipio',max_length=100)
	ambiente = models.CharField(max_length=1, choices=AMBIENTE_CHOICE)
	area = models.CharField('Area de Influencia',max_length=1,choices=AREA_CHOICE)
	contencao = models.CharField('Forma de Contencao',max_length=50)
	observacao = models.TextField('Observacoes relevantes',max_length=1000)
	

	def __unicode__(self):
	    return self.identificacao

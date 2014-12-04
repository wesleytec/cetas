#CADASTRO DE ANIMAIS NO SISTEMA
 
FILO_CHOICE = (
	('VER', 'Vertebrata'),
	('INV', 'Invertebrata'),
)
 
CLASSE_CHOICE = (
	('AMP', 'Amphibia'),
	('AVE', 'Aves'),
        ('INS', 'Insecta'),
	('MAM', 'Mammalia'),
	('PIS', 'Pisces'),
	('REP', 'Reptilia'),
)
 
ESTADO_CHOICE = (
	('1', 'vivo'),
	('2', 'obt campo'),
	('3', 'obt laboratorio'),
	('4', 'machucado'),
	('5', 'filhote'),
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
 
DESTINO_CHOICE = (
	('1', 'Soltura'),
	('2', 'Clinica'),
	('3', 'Descarte'),
	('4', 'Colecao Cientifica'),
)
 
class Animal(models.Model):
	    filo = models.CharField(max_length=3, choices=FILO_CHOICE)
        classe = models.CharField(max_length=3, choices=CLASSE_CHOICE)
        ordem = models.CharField(max_length=30)
        subordem = models.CharField('Subordem (Se Houver)',max_length=30)
        familia = models.CharField(max_length=30)
	    subfamilia = models.CharField('Subfamilia (Se Houver)',max_length=30)
        genero = models.CharField(max_length=30)
        especie = models.CharField(max_length=30)
        autor = models.CharField(max_length=30)
        nome = models.CharField('Nome Comum',max_length=50)
        
 
	def __unicode__(self):
	    return self.especie

class AnimalRegistry(models.Model):
        animal = models.ForeignKey(Animal)
        is_colection = models.BooleanField()
        estado = models.CharField(max_length=1, choices=ESTADO_CHOICE)
	    coleta = models.CharField('Local de Coleta',max_length=100)
	    Data = models.DateTimeField()
	    coletor = models.CharField(max_length=100)
	    latitude = models.IntegerField('Latitude',max_length=50)
        longitude = models.IntegerField('Longitude',max_length=50)
        municipio = models.CharField('Municipio',max_length=100)
	    ambiente = models.CharField(max_length=1, choices=AMBIENTE_CHOICE)
 	    area = models.CharField('Area de Influencia',max_length=1,choices=AREA_CHOICE)
	    ASV = models.CharField(max_length=50)
	    contencao = models.CharField('Forma de Contencao',max_length=50)
	    destino = models.CharField(max_length=1, choices=DESTINO_CHOICE)
	    observacao = models.TextField('Observacoes relevantes',max_length=1000)
 
    def __unicode__(self):
        return self.animal.name

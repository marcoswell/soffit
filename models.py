from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Usuario(models.Model):
    idu = models.IntegerField(null=False, blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)

    class Meta:
        abstract = True

class AvaliacaoFisica(models.Model):
    peso = models.DecimalField(blank=False , null = False, decimal_places=2, max_digits=5, validators=[MinValueValidator(0, "O valor deve ser maior que 0"), MaxValueValidator(250)])
    altura = models.DecimalField(blank=False , null = False, decimal_places=2, max_digits=5, validators=[MinValueValidator(0, "O valor deve ser maior que 0"), MaxValueValidator(250)])
    imc = models.DecimalField(decimal_places=2, max_digits=5)
    braco_d = models.DecimalField(blank=False , null = False, decimal_places=2, max_digits=5, validators=[MinValueValidator(0, "O valor deve ser maior que 0"), MaxValueValidator(400)])
    perna_e = models.DecimalField(blank=False , null = False, decimal_places=2, max_digits=5, validators=[MinValueValidator(0, "O valor deve ser maior que 0"), MaxValueValidator(400)]) 
    cintura = models.DecimalField(blank=False , null = False,decimal_places=2, max_digits=5, validators=[MinValueValidator(0, "O valor deve ser maior que 0"), MaxValueValidator(400)])
    comentario_af = models.CharField(max_length=500)

class EstadoFinanceiro(models.Model):

    STATUS = (
        ('Em Dia', 'Em Dia'),
        ('Inadimplente', 'Inadimplente'),
    )

    condicao = models.CharField(
        max_length=12,
        choices=STATUS,
    )

class Objetivo(models.Model):

    OBJS = (
        ('A Selecionar', 'A Selecionar'),
        ('Ganhar massa muscular', 'Ganhar massa muscular'),
        ('Emagrecer', 'Emagrecer'),
        ('Ganhar resistência', 'Ganhar resistência'),
    )

    opcao = models.CharField(
        max_length=21,
        choices=OBJS,
    )

    comentario = models.CharField(max_length=500)

class Aluno(Usuario): 
    avaliacao = models.ForeignKey(AvaliacaoFisica, on_delete=models.CASCADE)
    estadof = models.ForeignKey(EstadoFinanceiro, on_delete=models.CASCADE, null=True)
    objetivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE)
    frequencia = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Professor(Usuario):
    segunda_manha = models.BooleanField(default=False)
    segunda_tarde = models.BooleanField(default=False)
    segunda_noite = models.BooleanField(default=False)

    terca_manha = models.BooleanField(default=False)
    terca_tarde = models.BooleanField(default=False)
    terca_noite = models.BooleanField(default=False)

    quarta_manha = models.BooleanField(default=False)
    quarta_tarde = models.BooleanField(default=False)
    quarta_noite = models.BooleanField(default=False)

    quinta_manha = models.BooleanField(default=False)
    quinta_tarde = models.BooleanField(default=False)
    quinta_noite = models.BooleanField(default=False)

    sexta_manha = models.BooleanField(default=False)
    sexta_tarde = models.BooleanField(default=False)
    sexta_noite = models.BooleanField(default=False)

    sabado_manha = models.BooleanField(default=False)
    sabado_tarde = models.BooleanField(default=False)

    domingo_manha = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

#######################################################################################################

class cadastro_exer(models.Model): # cadastro dos exercicios disponiveis na academia
    nome_exercicio = models.CharField(max_length=50)

class Info_series(models.Model): # informaçoes das series: número de séries , tempo de intervalo 
     nome_exer = ( # costas
        ('puxada barra máquina', 'puxada barra máquina'),('puxada supinada(com pegada fechada)', 'puxada supinada(com pegada fechada)'),('barra fixa com triângulo', 'barra fixa com triângulo'),
        ('remada cavalinho', 'remada cavalinho'),('remada serrote', 'remada serrote'),('remada barra livre', 'remada barra livre'),
        ('pull over', 'pull over'),('remada na máquina', 'remada na máquina'),('crucifixo inverso máquina', 'crucifixo inverso máquina'),('crucifixo inverso halters', 'crucifixo inverso halters'),
        #biceps
        ('rosca scott', 'rosca scott'),('rosca concentrada', 'rosca concentrada'),('rosca unilateral', 'rosca unilateral'),('rosca barra', 'rosca barra'),('rosca barra 21', 'rosca barra 21'),
        ('rosca halter', 'rosca halter'),('rosca na maquina', 'rosca na maquina'),('rosca inversa', 'rosca inversa'),
        # peito
        ('supino reto', 'supino reto'),('supino inclinado', 'supino inclinado'),('supino declinado', 'supino declinado'),('cross over', 'cross over'),
        ('supino maquina', 'supino maquina'),('supino reto halter', 'supino reto halter'),
        ('supito inclinado halter', 'supito inclinado halter'),('crucifixo máquina', 'crucifixo máquina'),('crucifixo halters', 'crucifixo halters'),
        #triceps
        ('tríceps corda', 'tríceps corda'),('tríceps barra', 'tríceps barra'),('francês', 'francês'),('testa com barra', 'testa com barra'),('tríceps máquina', 'tríceps máquina'),
        #ombros
        ('elevação lateral', 'elevação lateral'),('elevação frontal', 'elevação frontal'),('elevação lateral cross over', 'elevação lateral cross over'),('desenvolvimento arnold', 'desenvolvimento arnold'),
        ('desenvolvimeto máquina', 'desenvolvimeto máquina'),('desenvolvimeto com halters', 'desenvolvimeto com halters'),
        # pernas
        ('cadeira extensora', 'cadeira extensora'),('cadeira extensora unilateral','cadeira extensora unilateral'),('cadeira flexora', 'cadeira flexora'),('mesa flexora', 'mesa flexora'),
        ('agachamento livre', 'agachamento livre'),('leg press 45', 'leg press 45'),('leg press horizontal', 'leg press horizontal'),('afundo com halters', 'afundo com halters'),
        ('agachamento smith', 'agachamento smith'),('panturrinha máquina(sentado)', 'panturrinha máquina(sentado)'),
        ('panturrilha em pé', 'panturrilha em pé'), ('panturrilha em pé unilateral', 'panturrilha em pé unilateral'),('cadeira adutora', 'cadeira adutora'),
        ('cadeira abdutora', 'cadeira abdutora'),('agachamento sumô', 'agachamento sumô'),
        # Abdomen
        ('abdominal máquina', 'abdominal máquina'),('abdominal', 'abdominal'),('elevação de pernas', 'elevação de pernas'),
        ('prancha abdominal', 'prancha abdominal'),('power wheel', 'power wheel'),('abdominal cruzado', 'abdominal cruzado'),
    )
    op_exer = models.CharField(
        max_length=3,
        choices=nome_exer,
    )
    num_series = (
        ('1 serie', '1 serie'),
        ('2 series', '2 series'),
        ('3 series', '3 series'),
        ('4 series', '4 series'),
        ('5 series', '5 series'),
        ('6 series', '6 series'),
    )
    op_series = models.CharField(
        max_length=3,
        choices=num_series,
    )
    tempo_intervalo = (
        ('30s', '30s'),
        ('45s', '45s'),
        ('1min', '1min'),
        ('1:30min', '1:30min'),
        ('1:45min', '1:45min'),
        ('2min', '2min'),
    )
    op_tempo = models.CharField(
        max_length=3,
        choices=tempo_intervalo,
    )
    comentario_exer = models.CharField(max_length=500)

class treino(models.Model):
     info_series = models.ForeignKey(Info_series, on_delete=models.CASCADE)
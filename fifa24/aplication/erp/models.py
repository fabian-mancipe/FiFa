from django.db import models

# Create your models here.

class team(models.Model):
    team_name = models.CharField(max_length=30, null=False, verbose_name='nombre_equipo')
    flag_image = models.ImageField(upload_to='banderas/', null=False, unique=True, verbose_name='banderas')
    shield_image = models.ImageField(upload_to='escudos/', null=False, unique=True, verbose_name='escudos')

def __str__(self):
    return self.name

class meta:
    db_table = 'equipo'
    verbose_name = 'equipo'
    verbose_name_plural = 'equipos'
    ordering = ['name']

class position(models.Model):
    name = models.CharField(max_length= 50, null= False, unique=True, verbose_name='nombre')
    description = models.TextField(null=False, unique=True, verbose_name='descripcion')

    def __str__(self):
        return self.name
    
    class meta:
        db_table = 'posicion'
        verbose_name = 'posicion'
        verbose_name_plural = 'posiciones'
        ordering =['id']


class player(models.Model):
    name = models.CharField(max_length=50, null=False, verbose_name='nombres')
    last_name = models.CharField(max_length=50, null=False, unique=True, verbose_name='apellidos')
    photo = models.ImageField(upload_to='jugador_photo/', null=False, unique=True, verbose_name='foto')
    birthdate = models.DateField(null=False, unique=True, verbose_name='fecha de nacimiento')
    position = models.ForeignKey(position, on_delete=models.CASCADE)
    number_shirt = models.PositiveIntegerField( null=False, unique=True, verbose_name='numero de camisa')
    headline = models.BooleanField( null=False, unique=True, verbose_name='titular')
    team = models.ForeignKey(team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'jugador'
        verbose_name = 'jugador'
        verbose_name_plural = 'jugadores'
        ordering = ['id']

    class Coach(models.Model):

        roles = (
        ('técnico', 'Técnico'),
        ('asistente', 'Asistente'),
        ('médico', 'Médico'),
        ('preparador', 'Preparador'),
    )
    
    PAISES_CHOICES = (
    ('BR', 'Brasil'),
    ('GER', 'Alemania'),
    ('ARG', 'Argentina'),
    ('ITA', 'Italia'),
    ('URU', 'Uruguay'),
    ('FRA', 'Francia'),
    ('ENG', 'Inglaterra'),
    ('ESP', 'España'),
    ('NED', 'Países Bajos'),
    ('POR', 'Portugal'),
    ('BEL', 'Bélgica'),
    ('SWE', 'Suecia'),
    ('CRO', 'Croacia'),
    ('RUS', 'Rusia'),
    ('DEN', 'Dinamarca'),
    ('MEX', 'México'),
    ('CHI', 'Chile'),
    ('COL', 'Colombia'),
    ('USA', 'Estados Unidos'),
    ('TUR', 'Turquía'),
    ('SUI', 'Suiza'),
    ('NGA', 'Nigeria'),
    ('CZE', 'República Checa'),
    ('CMR', 'Camerún'),
    ('GHA', 'Ghana'),
    ('SEN', 'Senegal'),
    ('AUS', 'Australia'),
    ('JPN', 'Japón'),
    ('KOR', 'Corea del Sur'),
    ('CRC', 'Costa Rica'),
    ('GRE', 'Grecia'),
    ('UKR', 'Ucrania'),
    ('PAR', 'Paraguay'),
    ('SRB', 'Serbia'),
    ('AUT', 'Austria'),
    ('ECU', 'Ecuador'),
    ('NOR', 'Noruega'),
    ('IRN', 'Irán'),
    ('MAR', 'Marruecos'),
    ('ROU', 'Rumanía'),
    ('BUL', 'Bulgaria'),
    ('SCO', 'Escocia'),
    ('WAL', 'Gales'),
    ('TUN', 'Túnez'),
    ('CAF', 'Costa de Marfil'),
    ('HUN', 'Hungría'),
    ('NZL', 'Nueva Zelanda'),
)

    name = models.CharField(max_length=50, verbose_name='Nombres')
    last_name = models.CharField(max_length=50, verbose_name='Apellidos')
    birthdate = models.DateField(verbose_name='Fecha_de_nacimiento')
    nationality = models.CharField(max_length=50, choices=PAISES_CHOICES, verbose_name='Nacionalidad')
    rol = models.CharField(max_length=20, choices=roles, verbose_name='Roles')
    equipo = models.OneToOneField(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.last_name}"

    class Meta:
        db_table = 'técnico'
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        ordering = ['id']
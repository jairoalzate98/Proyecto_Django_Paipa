from django.db import models
from django.forms import model_to_dict

# Create your models here.

class Carac(models.Model):
    municipios = models.CharField(max_length=100)
    areas = models.CharField(max_length=100)
    barrio_vereda = models.CharField(max_length=100)
    punt_sisb = models.DecimalField(max_digits=15, decimal_places=2)
    nivel_sisb = models.IntegerField()
    estrato = models.IntegerField()
    tipo_vivi = models.IntegerField()
    tenencia = models.IntegerField()
    sanitario = models.IntegerField()
    alumbrado = models.IntegerField()
    hacinami = models.CharField(max_length=100)
    gatos_cant = models.IntegerField()
    gatos_vacu = models.IntegerField()
    perros_can = models.IntegerField()
    perros_vac = models.IntegerField()
    equino_can = models.IntegerField()
    equino_vac = models.IntegerField()
    aves = models.IntegerField()
    porcinos = models.IntegerField()
    fuent_agua = models.IntegerField()
    acueducto = models.IntegerField()
    basuras = models.IntegerField()
    reci_basur = models.CharField(max_length=100)
    iluminacio = models.CharField(max_length=100)
    ventilacio = models.CharField(max_length=100)
    reservorio = models.CharField(max_length=100)
    anjeos = models.CharField(max_length=100)
    aseo = models.CharField(max_length=100)
    orden = models.CharField(max_length=100)
    piso_habit = models.IntegerField()
    piso_cocin = models.IntegerField()
    piso_bano = models.IntegerField()
    pare_habit = models.IntegerField()
    pare_cocin = models.IntegerField()
    pare_bano = models.IntegerField()

    def toJSON(self):
        item = model_to_dict(self)
        return item
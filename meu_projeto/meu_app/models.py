# models.py
from django.db import models

class Dados(models.Model):
    sensor = models.BooleanField(default=False)
    botao = models.BooleanField(default=False)
    liga_robo = models.BooleanField(default=False)
    reset_contador = models.BooleanField(default=False)
    valor_contagem = models.IntegerField(default=0)

    def ___str__(self):
            return f"Sensor: {self.sensor}, botao: {self.botao}, liga_robo: {self.liga_robo}, reset_contador: {self.reset_contador}, valor_contagem: {self.valor_contagem}"
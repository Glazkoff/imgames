from django.db import models
from apps.flows.models import Channel, Stage
from apps.rooms.models import Turn
from django.core.validators import MaxValueValidator, MinValueValidator


class ChannelComputed(models.Model):
    channel = models.ForeignKey(
        Channel, verbose_name="Изначальный канал", on_delete=models.CASCADE)
    turn = models.ForeignKey(
        Turn, verbose_name="Шаг пользователя", on_delete=models.CASCADE)
    cardinal_value = models.PositiveIntegerField("Входной трафик")

    def __str__(self):
        return f'ChannelComputed #{self.id}'

    class Meta:
        verbose_name = 'Просчитанный канал'
        verbose_name_plural = '[DEV] Просчитанные каналы'


class StageComputed(models.Model):
    stage = models.ForeignKey(
        Stage, verbose_name="Изначальный 'этап воронки'", on_delete=models.CASCADE)
    turn = models.ForeignKey(
        Turn, verbose_name="Шаг пользователя", on_delete=models.CASCADE)
    conversion = models.DecimalField(
        "Конверсия", decimal_places=2, max_digits=5, validators=[
            MaxValueValidator(100.00),
            MinValueValidator(0.01)
        ])
    cardinal_value = models.PositiveIntegerField("Входной трафик")

    def __str__(self):
        return f'ChannelComputed #{self.id}'

    class Meta:
        verbose_name = 'Просчитанный этап'
        verbose_name_plural = '[DEV] Просчитанные этапы'

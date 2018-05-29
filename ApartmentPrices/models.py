from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from .calculator import calculate
from django.utils.translation import gettext_lazy as _
    
class Material(models.Model):
    name_mtrl = models.CharField(max_length=20, unique=True, verbose_name=u"Название")
    def __str__(self):
        return self.name_mtrl
    class Meta:
        verbose_name = u'Материал дома'
        verbose_name_plural = u'Материалы дома'

class District(models.Model):
    name_dstr = models.CharField(max_length=20, unique=True, verbose_name=u"Название")
    def __str__(self):
        return self.name_dstr
    class Meta:
        verbose_name = u'Район'
        verbose_name_plural = u'Районы'

class Apartment(models.Model):
    room_no = models.PositiveIntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name=u"Количество комнат")
    area = models.PositiveIntegerField(default=50, validators=[MinValueValidator(10), MaxValueValidator(1000)], verbose_name=u"Площадь")
    first_floor = models.BooleanField(verbose_name=u"На 1-м этаже?")
    last_floor = models.BooleanField(verbose_name=u"На последнем этаже?")
    balcony = models.BooleanField(default=False, verbose_name=u"Есть балкон?")
    total_floors = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name=u"Всего этажей")
    h_mtrl = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name=u"Материал дома")
    h_dstr = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name=u"Район")
    def _get_price(self):
        return '%0.2f' % calculate(self.h_dstr_id, self.h_mtrl_id,
                self.total_floors, self.first_floor, self.last_floor,
                self.room_no, self.area, self.balcony)
    _get_price.short_description = u'Стоимость'
    price = property(_get_price)
    def clean(self):
        if self.area < self.room_no * 10:
            raise ValidationError(_('Площадь должна быть не меньше значения: Количество комнат * 10 !'))
        if self.total_floors == 2 and not(self.first_floor) and not(self.last_floor):
            raise ValidationError(_('Всего этажей вы выбрали 2. Отметьте первый или последний этаж !'))
        if self.total_floors == 1 and (self.first_floor or self.last_floor):
            raise ValidationError(_('Всего этажей вы выбрали 1. Уберите отметки у первого и последнего этажа !'))
        if self.first_floor and self.last_floor:
            raise ValidationError(_('Вы выбрали и первый, и последний этаж. Отметьте один вариант !'))
    def __str__(self):
        return "Квартира "+str(self.id)
    class Meta:
        verbose_name = u'Квартира'
        verbose_name_plural = u'Квартиры'

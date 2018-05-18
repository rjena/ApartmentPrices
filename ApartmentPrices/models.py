from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from .calculator import calculate
from django.utils.translation import gettext_lazy as _

def validate_nonzero(value):
    if value == 0:
        raise ValidationError(
            ('Это значение не может быть равно 0'),
            params={'value': value},
        )
    
class Material(models.Model):
    name_mtrl = models.CharField(max_length=20)
    def __str__(self):
        return self.name_mtrl
    class Meta:
        verbose_name = u'Материал дома'
        verbose_name_plural = u'Материал дома'

class District(models.Model):
    name_dstr = models.CharField(max_length=20)
    def __str__(self):
        return self.name_dstr
    class Meta:
        verbose_name = u'Район'
        verbose_name_plural = u'Район'

class Apartment(models.Model):
    room_no = models.PositiveIntegerField(default=2, validators=[MaxValueValidator(20), validate_nonzero], verbose_name=u"Количество комнат")
    area = models.DecimalField(default=50.00, decimal_places=2, max_digits=5, verbose_name=u"Площадь")
    first_floor = models.BooleanField(verbose_name=u"На 1-м этаже?")
    last_floor = models.BooleanField(verbose_name=u"На последнем этаже?")
    balcony = models.BooleanField(default=False, verbose_name=u"Есть балкон?")
    total_floors = models.PositiveIntegerField(default=5, validators=[MaxValueValidator(100), validate_nonzero], verbose_name=u"Всего этажей")
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
    def __str__(self):
        return "Квартира "+str(self.id)
    class Meta:
        verbose_name = u'Квартира'
        verbose_name_plural = u'Квартира'

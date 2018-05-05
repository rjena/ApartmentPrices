from django.db import models

class Room(models.Model):
    quantity = models.IntegerField(default=0)
    def __str__(self):
    	if self.quantity<5:
    		return str(self.quantity)
    	else:
    		return str(self.quantity)+" и более"
    class Meta:
        verbose_name = u'Количество комнат'
        verbose_name_plural = u'Количество комнат'

class Floor(models.Model):
    from_no = models.IntegerField(default=0)
    to_no = models.IntegerField(default=3)
    def __str__(self):
        return str(self.from_no)+" - "+str(self.to_no)
    class Meta:
        verbose_name = u'Этаж'
        verbose_name_plural = u'Этаж'

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
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name=u"Количество комнат")
    first_floor = models.BooleanField(verbose_name=u"На 1-м этаже?")
    last_floor = models.BooleanField(verbose_name=u"На последнем этаже?")
    balcony = models.BooleanField(default=False, verbose_name=u"Есть балкон?")
    ap_floor = models.ForeignKey(Floor, on_delete=models.CASCADE, verbose_name=u"Этаж")
    h_mtrl = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name=u"Материал дома")
    h_dstr = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name=u"Район")
    price = models.FloatField(verbose_name=u"Стоимость")
    def __str__(self):
        return "Квартира "+str(self.id)
    class Meta:
        verbose_name = u'Квартира'
        verbose_name_plural = u'Квартира'

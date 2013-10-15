from django.db import models

# Create your models here.


class FlowerPiAddress(models.Model):
    ip_address = models.IPAddressField()
    date = models.DateTimeField('date of address update')
    def __unicode__(self):
        return self.ip_address

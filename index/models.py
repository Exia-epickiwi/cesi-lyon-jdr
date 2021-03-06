# -*- coding: utf-8 -*-
from django.db import models

class Setting(models.Model):

    key = models.CharField(max_length=255,verbose_name="Clé")
    value = models.CharField(max_length=255,verbose_name="Valeur")

    def __unicode__(self):
        """renvoie la clé"""

        return self.key
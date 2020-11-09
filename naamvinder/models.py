from django.db import models
from solo.models import SingletonModel
from django.contrib.postgres.fields import ArrayField

# Naam veur ein van de deelnemers
class Naam(models.Model):
    """
    Model for recording a name
    """
    naam = models.CharField(max_length=40)

    def __str__(self):
        return '******'

# Admin Settings
class Config(SingletonModel):
    """
    Singelton model for global settings
    """

    # Email for sending result to
    destinationEmail = models.CharField(max_length=128, default="")

    # List of known deelnemers
    deelnemers = ArrayField(
        models.CharField(max_length=40),
        size=7,
        default=list
    )

    # Has self-destuction been carried out
    selfDestroyed = models.BooleanField(default=False)

    def destroy(self):
        self.selfDestroyed = True
        self.save()
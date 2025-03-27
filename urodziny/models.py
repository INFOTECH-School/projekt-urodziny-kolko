from django.db import models

# Create your models here.
class Solenizant(models.Model):
    wiek = models.IntegerField(default=18)
    stan_upojenia = models.CharField(choices={
        "1" : "Aldente",
        "2" : "Pada",
        "3" : "Ze mną się nie napijesz?",
        "4" : "Stary krecik mocno śpi"
    },max_length=50)
    data_urodzin = models.DateTimeField()
    zdjecie1 = models.ImageField(upload_to="images/")
    zdjecie2 = models.ImageField(upload_to="images/")
    zdjecie3 = models.ImageField(upload_to="images/")
    zdjecie4 = models.ImageField(upload_to="images/")

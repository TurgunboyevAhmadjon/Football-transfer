from django.db import models


class Clubs(models.Model):
    nom = models.CharField(max_length=50)
    president = models.CharField(max_length=50)
    coach = models.CharField(max_length=100)
    davlat = models.CharField(max_length=50)
    yil = models.DateTimeField()
    record_transfer = models.CharField(max_length=100)
    record_arrival = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Player(models.Model):
    ism = models.CharField(max_length=100)
    yosh = models.IntegerField(blank=True)
    davlat = models.CharField(max_length=50)
    pozitsiya = models.CharField(max_length=100)
    narx = models.IntegerField()
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism


class Transfers(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    all_from = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name='al_from')
    all_to = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name='al_to')
    tah_narx = models.IntegerField()
    narx = models.IntegerField()
    mavsum = models.CharField(max_length=200)
    def __str__(self):
        return self.mavsum






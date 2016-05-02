from django.db import models



class Game_type(models.Model):
    game_type = models.CharField(max_length=20)

    def __str__(self):
        return self.game_type


class Games(models.Model):
    title = models.CharField(max_length=20)
    game_type = models.ForeignKey(Game_type, on_delete=models.CASCADE)
    game_description = models.CharField(max_length=1000)
    game_mytype = models.CharField(max_length=40) #opis stylu gry

from django.db import models

class Scheduling(models.Model):
    name = models.CharField(max_length=50)
    cpf = models.PositiveIntegerField()
    date = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    querycovid = models.PositiveIntegerField(default=0) #inicialmente ninguem tem resultado de exame no sistema. 

    def __str__(self):
        return self.name

    def exam(self):
        if bool(self.querycovid) == True :
            return 'Voce possui resultados de exames'
        else:
            return 'Sem resultados de exames' 


from django.db import models

class Scheduling(models.Model):
    name = models.CharField(max_length=50)
    categoryUser = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    cpf = models.PositiveIntegerField()
    date = models.CharField(max_length=10, null=True)
    description = models.CharField(blank=True, null=True, max_length=500)
    
    

    def __str__(self):
        return self.name

    def exam(self):
        if bool(self.description) == True :
            return 'Voce possui resultados de exames'
        else:
            return 'Sem resultados de exames' 


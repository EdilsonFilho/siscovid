from .models import Scheduling
from rest_framework import serializers




class SchedulingSerializer(serializers.ModelSerializer):
    exam = serializers.ReadOnlyField() #Aqui mostro true se o cidadao tiver alguma exame com resultado no sistema
    
    class Meta: 
        model = Scheduling
        exclude = ['querycovid']
    
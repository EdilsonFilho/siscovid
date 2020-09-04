from rest_framework import viewsets
from .serializers import SchedulingSerializer

from .models import Scheduling

class SchedulingViewSet(viewsets.ModelViewSet):

    serializer_class = SchedulingSerializer
    queryset = Scheduling.objects.all()



    



        


     


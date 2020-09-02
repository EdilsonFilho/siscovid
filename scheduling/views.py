from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import SchedulingSerializer
from .models import Scheduling

class SchedulingApiView(ListAPIView):
    """
    Use esse endereço para gerenciar os agendamentos de consultas
    """
    queryset = Scheduling.objects.all()
    serializer_class = SchedulingSerializer

class SchedulingCreateView(CreateAPIView):
    queryset = Scheduling.objects.all()
    serializer_class = SchedulingSerializer
    
scheduling_view = SchedulingApiView.as_view()
scheduling_create_view = SchedulingCreateView.as_view()

    



        


     


from django.views.generic import ListView
from .models import Incident

class MapView(ListView):
    model = Incident
    template_name = 'incidents/map.html'
    context_object_name = 'incidents'
from rest_framework import generics
from .models import Beneficiaire
from .serializers import BeneficiaireSerializer
from django.db.models import prefetch_related_objects

class BeneficiaireListView(generics.ListAPIView):
    serializer_class = BeneficiaireSerializer
    
    def get_queryset(self):
        queryset = Beneficiaire.objects.all()
        # Optimisation des requêtes
        prefetch_related_objects(queryset, 'utilisateur')
        return queryset
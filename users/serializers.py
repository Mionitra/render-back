from rest_framework import serializers
from .models import Beneficiaire

class BeneficiaireSerializer(serializers.ModelSerializer):
    nom_complet = serializers.SerializerMethodField()
    telephone = serializers.CharField(source='utilisateur.telephone')
    photo = serializers.CharField(source='utilisateur.photo_url')

    class Meta:
        model = Beneficiaire
        fields = [
            'id',
            'nom_complet',
            'telephone',
            'photo',
            'revenu_mensuel',
            'nombre_enfants',
            'statut_familial',
            'fokontany'
        ]

    def get_nom_complet(self, obj):
        return f"{obj.utilisateur.nom}"
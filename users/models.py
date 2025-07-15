from django.db import models

class Utilisateur(models.Model):
    ROLES = (
        ('BENEFICIAIRE', 'Bénéficiaire'),
        ('ADMIN', 'Administrateur'),
    )
    
    nom = models.CharField(max_length=100)
    # prenom = models.CharField(max_length=100) 
    telephone = models.CharField(max_length=20)
    cin = models.CharField(max_length=20, unique=True)
    photo_url = models.URLField(max_length=255, blank=True)
    role = models.CharField(max_length=20, choices=ROLES, default='BENEFICIAIRE')

    def __str__(self):
        return f"{self.nom} ({self.cin})"

class Beneficiaire(models.Model):
    STATUTS_FAMILIAUX = (
        ('célibataire', 'Célibataire'),
        ('marié', 'Marié(e)'),
        ('veuf', 'Veuf/Veuve'),
    )
    
    utilisateur = models.OneToOneField(
        Utilisateur, 
        on_delete=models.CASCADE,
        related_name='beneficiaire'
    )
    revenu_mensuel = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_enfants = models.PositiveIntegerField()
    statut_familial = models.CharField(max_length=20, choices=STATUTS_FAMILIAUX)
    conjoint = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    fokontany = models.CharField(max_length=50)

    def __str__(self):
        return f"Bénéficiaire {self.utilisateur.nom}"
import random
from django.core.management.base import BaseCommand
from users.models import Utilisateur, Beneficiaire

class Command(BaseCommand):
    help = 'Génère des utilisateurs et bénéficiaires fictifs'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=100,
            help='Nombre d\'utilisateurs à générer'
        )

    def generate_cin(self):
        return "{:02d}{:02d}{:03d}{:03d}{:02d}".format(
            random.randint(1, 99),
            random.randint(50, 99),
            random.randint(100, 999),
            random.randint(100, 999),
            random.randint(10, 99)
        )

    def handle(self, *args, **options):
        count = options['count']
        fokontany_list = ["Anosibe", "Isotry", "Analakely", "Andraisora", "Soamanandrariny", 
                         "Malaza Ampitatafika", "Ambohitsoa", "Analamahitsy", "Ankeniheny",
                         "Ankazotoho", "Anosizato Andrefana", "Fiadanana", "Ankadifotsy", "Ifarihy"]
        
        # Création des utilisateurs
        utilisateurs = []
        for i in range(1, count + 1):
            user = Utilisateur.objects.create(
                nom=f"Nom{i}",
                telephone=f"034{random.randint(1000000, 9999999)}",
                cin=self.generate_cin(),
                photo_url="https://picsum.photos/200",
                role="BENEFICIAIRE"
            )
            utilisateurs.append(user)
        
        # Création des bénéficiaires
        beneficiaires = []
        for user in utilisateurs:
            statut = random.choice(["célibataire", "marié", "veuf"])
            benef = Beneficiaire.objects.create(
                utilisateur=user,
                revenu_mensuel=random.randint(50000, 500000),
                nombre_enfants=random.randint(0, 5),
                statut_familial=statut,
                fokontany=random.choice(fokontany_list)
            )
            beneficiaires.append(benef)
        
        # Lier les conjoints
        maries_sans_conjoint = [
            b for b in beneficiaires 
            if b.statut_familial == "marié" and b.conjoint is None
        ]
        
        while len(maries_sans_conjoint) >= 2:
            b1 = maries_sans_conjoint.pop()
            b2 = maries_sans_conjoint.pop()
            b1.conjoint = b2
            b2.conjoint = b1
            b1.save()
            b2.save()
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully generated {count} utilisateurs with beneficiaires'))
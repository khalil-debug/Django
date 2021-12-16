from django.db import models

# Create your models here.
from django.db.models.fields import DecimalField
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




# Create your models here.
class Groupe(models.Model):
    nom_groupe = models.CharField(max_length=200)
    nbrEtud = models.IntegerField(default=0)
    email_gr = models.CharField(max_length=200)
    niveauEtud = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nom_groupe
   
    

class Etudiant(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    idGroup = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    nom_etudiant= models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance= models.DateField(default=timezone.now)
    photo=models.ImageField(null=True,blank=True,upload_to=dir)
    adrMail=models.EmailField()
    etat= models.CharField(max_length=50)
    situation=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.nom_etudiant

class  Module(models.Model) : 
      nom_module= models.CharField(max_length=200,unique=True)
      nbtotalH = models.IntegerField(default=0)
      type = models.CharField(max_length=50)
      niveau = models.IntegerField(default=1)
      idGroup=models.ManyToManyField(Groupe)
      def __str__(self):
        return self.nom_module
    

class Seance(models.Model):
    idMod = models.ForeignKey(Module, on_delete=models.CASCADE)
    Hdebut=models.DateTimeField('date debut')
    Hfin=models.DateTimeField('date fin')
    NumSalle= models.IntegerField(default=1)
    objectif=models.CharField(max_length=200)
    resume=models.CharField(max_length=800)
    etat=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    def __str__(self):
        return self.objectif


class Absence(models.Model) : 
    Date=models.DateTimeField('date absence')
    justif=models.CharField(max_length=500)
    idetudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    idseance= models.ForeignKey(Seance, on_delete=models.CASCADE)
    def __str__(self):
        return self.justif


class Enregistrement(models.Model) : 
      idseance= models.ForeignKey(Seance, on_delete=models.CASCADE)
      nom_enregistrement=models.CharField(max_length=50,unique=True)
      URL=models.URLField(max_length=100)
      type=models.CharField(max_length=50)
      contenu=models.CharField(max_length=200)
      description=models.CharField(max_length=500)
      def __str__(self):
        return self.nom_enregistrement



class Enseignant(models.Model) :
    user= models.OneToOneField(User, on_delete=models.CASCADE, default="")
    nom_enseignant = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mailPers=models.EmailField()
    mailTravail=models.EmailField()
    du=models.IntegerField(default=1)
    photo=models.ImageField(null=True,blank=True,upload_to=dir)
    Ens_Mod=models.ManyToManyField(Module)
    def __str__(self):
        return self.nom_enseignant

    
class trav_a_rendre(models.Model) :
    idMod = models.ForeignKey(Module, on_delete=models.CASCADE)
    titre= models.CharField(max_length=200)
    date_lance=models.DateField(default=timezone.now)
    nature= models.CharField(max_length=200)
    description=models.CharField(max_length=600)
    DDL=models.DateTimeField('date DDL')
    Attach_Enonce= models.FileField(upload_to=dir)
    Attach_Rendu= models.FileField(upload_to=dir)
    etat= models.CharField(max_length=100)
    evaluation=models.CharField(max_length=600)
    def __str__(self):
        return self.titre
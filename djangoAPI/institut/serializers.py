#ce fichier permet de traduire les variables des classes en Json 

from django.contrib.auth.models import Group, User
from django.db.models import fields
from rest_framework import serializers
from .models import Absence, Enregistrement, Enseignant, Etudiant, Groupe, Module, Seance, trav_a_rendre

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Etudiant
        fields=('id', 'nom_etudiant', 'prenom', 'date_naissance', 'photo',
         'adrMail', 'etat', 'situation', 'idGroup','user')

class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Groupe
        fields=('id','nom_groupe','nbrEtud','email_gr','niveauEtud')

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Module
        fields=('id','nom_module','nbtotalH','type','niveau','idGroup')

class SeanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seance
        fields=('id','idMod','Hdebut','Hfin','NumSalle','objectif',
        'resume','etat','type')


class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Absence
        fields=('id','Date','justif','idetudiant','idseance')

class EnregSerializer(serializers.ModelSerializer):
    class Meta:
        model= Enregistrement
        fields=('id','idseance','nom_enregistrement','URL','type',
        'contenu','description')

class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model= Enseignant
        fields=('id','nom_enseignant','prenom','mailPers','mailTravail',
        'du','photo','Ens_Mod','user')

class TarSerializer(serializers.ModelSerializer):
    class Meta:
        model= trav_a_rendre
        fields=('id','idMod','titre','date_lance','nature','evaluation',
        'description','DDL','Attach_Enonce','Attach_Rendu','etat')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
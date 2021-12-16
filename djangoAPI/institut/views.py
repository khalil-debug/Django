from django.shortcuts import render

from django.http.response import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.files.storage import default_storage

from .models import *
from .serializers import *
# Create your views here.
#api des etudiants
@csrf_exempt
def EtudiantAPI(request,id=0):
    if request.method=='GET':
        etudiants=Etudiant.objects.all()
        etudiant_serializer= EtudiantSerializer(etudiants,many=True)
        return JsonResponse(etudiant_serializer.data,safe=False)

    elif request.method=='POST':
        etudiant_data=JSONParser().parse(request)
        etudiant_serializer=EtudiantSerializer(data=etudiant_data)
        if etudiant_serializer.is_valid():
            etudiant_serializer.save()
            return JsonResponse("Etudiant ajouté avec Succés",safe=False)
        return JsonResponse("Verifiez vos données!")

    elif request.method=='PUT':
        etudiant_data=JSONParser().parse(request)
        etudiant= Etudiant.objects.get(idEtud=etudiant_data['id'])
        etudiant_serializer=EtudiantSerializer(etudiant,data=etudiant_data)
        if etudiant_serializer.is_valid():
            etudiant_serializer.save()
            return JsonResponse("Etudiant modifié avec Succés!", safe=False)
        return JsonResponse("Verifiez vos données!",safe=False)
    
    elif request.method=='DELETE':
        etudiant=Etudiant.objects.get(idEtud=id)
        etudiant.delete()
        return JsonResponse("Supprimé!",safe=False)

#api des enseignants
@csrf_exempt
def EnseignantAPI(request,id=0):
    if request.method=='GET':
        ens=Enseignant.objects.all()
        ens_serializer= EnseignantSerializer(ens,many=True)
        return JsonResponse(ens_serializer.data,safe=False)

    elif request.method=='POST':
        ens_data=JSONParser().parse(request)
        ens_serializer=EnseignantSerializer(data=ens_data)
        if ens_serializer.is_valid():
            ens_serializer.save()
            return JsonResponse("Enseignant ajouté avec Succés",safe=False)
        return JsonResponse("Verifiez vos données!")

    elif request.method=='PUT':
        ens_data=JSONParser().parse(request)
        enseignant= Enseignant.objects.get(idEns=ens_data['id'])
        ens_serializer=EnseignantSerializer(enseignant,data=ens_data)
        if ens_serializer.is_valid():
            ens_serializer.save()
            return JsonResponse("Enseignant modifié avec Succés!", safe=False)
        return JsonResponse("Verifiez vos données!",safe=False)
    
    elif request.method=='DELETE':
        enseignant=Enseignant.objects.get(idEns=id)
        enseignant.delete()
        return JsonResponse("Supprimé!",safe=False)

#api des groupes
@csrf_exempt
def GroupeAPI(request,id=0):
    if request.method=='GET':
        grp=Groupe.objects.all()
        grp_serializer= GroupeSerializer(grp,many=True)
        return JsonResponse(grp_serializer.data,safe=False)

    elif request.method=='POST':
        grp_data=JSONParser().parse(request)
        grp_serializer=GroupeSerializer(data=grp_data)
        if grp_serializer.is_valid():
            grp_serializer.save()
            return JsonResponse("Groupe ajouté avec Succés",safe=False)
        return JsonResponse("Verifiez vos données!")

    elif request.method=='PUT':
        grp_data=JSONParser().parse(request)
        groupe= Groupe.objects.get(idGrp=grp_data['id'])
        grp_serializer=GroupeSerializer(groupe,data=grp_data)
        if grp_serializer.is_valid():
            grp_serializer.save()
            return JsonResponse("Groupe modifié avec Succés!", safe=False)
        return JsonResponse("Verifiez vos données!",safe=False)
    
    elif request.method=='DELETE':
        groupe=Groupe.objects.get(idGrp=id)
        groupe.delete()
        return JsonResponse("Supprimé!",safe=False)

#api des modules
@csrf_exempt
def ModuleAPI(request,id=0):
    if request.method=='GET':
        mod=Module.objects.all()
        mod_serializer= ModuleSerializer(mod,many=True)
        return JsonResponse(mod_serializer.data,safe=False)

    elif request.method=='POST':
        mod_data=JSONParser().parse(request)
        mod_serializer=ModuleSerializer(data=mod_data)
        if mod_serializer.is_valid():
            mod_serializer.save()
            return JsonResponse("Module ajouté avec Succés",safe=False)
        return JsonResponse("Verifiez vos données!")

    elif request.method=='PUT':
        mod_data=JSONParser().parse(request)
        module= Module.objects.get(idMod=mod_data['id'])
        mod_serializer=ModuleSerializer(module,data=mod_data)
        if mod_serializer.is_valid():
            mod_serializer.save()
            return JsonResponse("Module modifié avec Succés!", safe=False)
        return JsonResponse("Verifiez vos données!",safe=False)
    
    elif request.method=='DELETE':
        module=Module.objects.get(idMod=id)
        module.delete()
        return JsonResponse("Supprimé!",safe=False)

#api des seance
@csrf_exempt
def SeanceAPI(request,id=0):
    if request.method=='GET':
        seance=Seance.objects.all()
        seance_serializer= SeanceSerializer(seance,many=True)
        return JsonResponse(seance_serializer.data,safe=False)

    elif request.method=='POST':
        seance_data=JSONParser().parse(request)
        seance_serializer=SeanceSerializer(data=seance_data)
        if seance_serializer.is_valid():
            seance_serializer.save()
            return JsonResponse("Séance ajouté avec Succés",safe=False)
        return JsonResponse("Verifiez vos données!")

    elif request.method=='PUT':
        seance_data=JSONParser().parse(request)
        seance= Seance.objects.get(idSce=seance_data['id'])
        seance_serializer=SeanceSerializer(seance,data=seance_data)
        if seance_serializer.is_valid():
            seance_serializer.save()
            return JsonResponse("Séance modifié avec Succés!", safe=False)
        return JsonResponse("Verifiez vos données!",safe=False)
    
    elif request.method=='DELETE':
        seance=Seance.objects.get(idSce=id)
        seance.delete()
        return JsonResponse("Supprimé!",safe=False)

#api des absences
@csrf_exempt
def AbsenceAPI(request,id=0):
    if request.method=='GET':
        abs=Absence.objects.all()
        abs_serializer= AbsenceSerializer(abs,many=True)
        return JsonResponse(abs_serializer.data,safe=False)

    elif request.method=='POST':
        abs_data=JSONParser().parse(request)
        abs_serializer=AbsenceSerializer(data=abs_data)
        if abs_serializer.is_valid():
            abs_serializer.save()
            return JsonResponse("Absence ajouté avec Succés",safe=False)
        return JsonResponse("Verifiez vos données!")

    elif request.method=='PUT':
        abs_data=JSONParser().parse(request)
        absence= Absence.objects.get(idAbs=abs_data['id'])
        abs_serializer=AbsenceSerializer(absence,data=abs_data)
        if abs_serializer.is_valid():
            abs_serializer.save()
            return JsonResponse("Absence modifié avec Succés!", safe=False)
        return JsonResponse("Verifiez vos données!",safe=False)
    
    elif request.method=='DELETE':
        absence=Absence.objects.get(idAbs=id)
        absence.delete()
        return JsonResponse("Supprimé!",safe=False)

#api des enregistrements
@csrf_exempt
def EnregistrementAPI(request,id=0):
    if request.method=='GET':
        enr=Enregistrement.objects.all()
        enr_serializer= EnregSerializer(enr,many=True)
        return JsonResponse(enr_serializer.data,safe=False)

    elif request.method=='POST':
        enr_data=JSONParser().parse(request)
        enr_serializer=EnregSerializer(data=enr_data)
        if enr_serializer.is_valid():
            enr_serializer.save()
            return JsonResponse("Enregistrement ajouté avec Succés",safe=False)
        return JsonResponse("Verifiez vos données!")

    elif request.method=='PUT':
        enr_data=JSONParser().parse(request)
        enregistrement= Enregistrement.objects.get(idEnr=enr_data['id'])
        enr_serializer=EnregSerializer(enregistrement,data=enr_data)
        if enr_serializer.is_valid():
            enr_serializer.save()
            return JsonResponse("Enregistrement modifié avec Succés!", safe=False)
        return JsonResponse("Verifiez vos données!",safe=False)
    
    elif request.method=='DELETE':
        enregistrement=Enregistrement.objects.get(idEnr=id)
        enregistrement.delete()
        return JsonResponse("Supprimé!",safe=False)

#api des travail à rendre
@csrf_exempt
def Trav_A_RendreAPI(request,id=0):
    if request.method=='GET':
        Tar=trav_a_rendre.objects.all()
        tar_serializer= TarSerializer(Tar,many=True)
        return JsonResponse(tar_serializer.data,safe=False)

    elif request.method=='POST':
        tar_data=JSONParser().parse(request)
        tar_serializer=TarSerializer(data=tar_data)
        if tar_serializer.is_valid():
            tar_serializer.save()
            return JsonResponse("Travail à rendre ajouté avec Succés",safe=False)
        return JsonResponse("Verifiez vos données!")

    elif request.method=='PUT':
        tar_data=JSONParser().parse(request)
        tar= trav_a_rendre.objects.get(idtar=tar_data['id'])
        tar_serializer=TarSerializer(tar,data=tar_data)
        if tar_serializer.is_valid():
            tar_serializer.save()
            return JsonResponse("Module modifié avec Succés!", safe=False)
        return JsonResponse("Verifiez vos données!",safe=False)
    
    elif request.method=='DELETE':
        tar=trav_a_rendre.objects.get(idtar=id)
        tar.delete()
        return JsonResponse("Supprimé!",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name= default_storage.save(file.name,file)
    
    return JsonResponse(file_name,safe=False)
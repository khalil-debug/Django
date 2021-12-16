from django.conf.urls.static import static
from django.urls.conf import path
from institut import views
from django.conf import settings

urlpatterns=[
    path('etudiant/', views.EtudiantAPI),
    path('etudiant/([0-9]+)', views.EtudiantAPI),
    path('enseignant/', views.EnseignantAPI),
    path('groupe/', views.GroupeAPI),
    path('seance/', views.SeanceAPI),
    path('module/', views.ModuleAPI),
    path('absence/', views.AbsenceAPI),
    path('enreg/', views.EnregistrementAPI),
    path('tar/', views.Trav_A_RendreAPI),
    path('SaveFile/', views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
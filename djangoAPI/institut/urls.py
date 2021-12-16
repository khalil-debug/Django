from django.conf.urls.static import static
from django.urls.conf import path
from institut import views
from django.conf import settings

urlpatterns=[
    path('etudiant/', views.EtudiantView.as_view()),
    path('enseignant/', views.EnregView.as_view()),
    path('groupe/', views.GroupeView.as_view()),
    path('seance/', views.SeanceView.as_view),
    path('module/', views.ModuleView.as_view()),
    path('absence/', views.AbsenceView.as_view()),
    path('enreg/', views.EnregView.as_view()),
    path('tar/', views.TarView.as_view()),
] 
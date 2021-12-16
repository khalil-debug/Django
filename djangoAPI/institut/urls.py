from django.conf.urls.static import static
from django.urls.conf import path
from institut import views
from django.conf import settings

urlpatterns=[
    path('etudiant/', views.GroupeAPI),
    path('etudiant/([0-9]+)', views.GroupeAPI),

    path('SaveFile/', views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Generated by Django 4.0 on 2021-12-15 22:55

import builtins
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_groupe', models.CharField(max_length=200)),
                ('nbrEtud', models.IntegerField(default=0)),
                ('email_gr', models.CharField(max_length=200)),
                ('niveauEtud', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_module', models.CharField(max_length=200, unique=True)),
                ('nbtotalH', models.IntegerField(default=0)),
                ('type', models.CharField(max_length=50)),
                ('niveau', models.IntegerField(default=1)),
                ('idGroup', models.ManyToManyField(to='institut.Groupe')),
            ],
        ),
        migrations.CreateModel(
            name='trav_a_rendre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('date_lance', models.DateField(default=django.utils.timezone.now)),
                ('nature', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=600)),
                ('DDL', models.DateTimeField(verbose_name='date DDL')),
                ('Attach_Enonce', models.FileField(upload_to=builtins.dir)),
                ('Attach_Rendu', models.FileField(upload_to=builtins.dir)),
                ('etat', models.CharField(max_length=100)),
                ('evaluation', models.CharField(max_length=600)),
                ('idMod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institut.module')),
            ],
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hdebut', models.DateTimeField(verbose_name='date debut')),
                ('Hfin', models.DateTimeField(verbose_name='date fin')),
                ('NumSalle', models.IntegerField(default=1)),
                ('objectif', models.CharField(max_length=200)),
                ('resume', models.CharField(max_length=800)),
                ('etat', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('idMod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institut.module')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_etudiant', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('date_naissance', models.DateField(default=django.utils.timezone.now)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=builtins.dir)),
                ('adrMail', models.EmailField(max_length=254)),
                ('etat', models.CharField(max_length=50)),
                ('situation', models.CharField(max_length=50)),
                ('idGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institut.groupe')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_enseignant', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('mailPers', models.EmailField(max_length=254)),
                ('mailTravail', models.EmailField(max_length=254)),
                ('du', models.IntegerField(default=1)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=builtins.dir)),
                ('Ens_Mod', models.ManyToManyField(to='institut.Module')),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Enregistrement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_enregistrement', models.CharField(max_length=50, unique=True)),
                ('URL', models.URLField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('contenu', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('idseance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institut.seance')),
            ],
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(verbose_name='date absence')),
                ('justif', models.CharField(max_length=500)),
                ('idetudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institut.etudiant')),
                ('idseance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institut.seance')),
            ],
        ),
    ]

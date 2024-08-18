from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
############CAMION #############
class Camion(models.Model):
    id_cam = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    immatriculation = models.CharField(max_length=20)
    transporteur = models.TextField()
    def str(self):
        return f"Camion {self.id_cam} "
############ MOUVEMENT #############
class Mouvement1(models.Model):
    id_mvt = models.AutoField(primary_key=True)
    statut_entree = models.IntegerField()
    statut_sortie = models.IntegerField(null=True, blank=True)
    date_sortie = models.DateTimeField(null=True, blank=True)
    date_entree = models.DateTimeField(null=True, blank=True)
    ########## INTEGRATION  DES POINTEUR ############
    pointeur_entree = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_entree', null=True, blank=True)
    pointeur_sortie = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_sortie', null=True, blank=True)
    ########## INTEGRATION  DES CAMIONS ############
    camion = models.ForeignKey('Camion', on_delete=models.CASCADE, related_name='mouvements', null=True, blank=True)
    ###chauffeur
    chauffeur = models.ForeignKey('Chaffeur', on_delete=models.CASCADE, related_name='mouvements', null=True, blank=True)
    #####Mouvement0
    ###chauffeur
    id_mvt_0 = models.ForeignKey('Mouvement0', on_delete=models.CASCADE, related_name='mouvements', null=True,
                                  blank=True)

    remorque = models.CharField(max_length=255,null=True)
    mission = models.CharField(max_length=255, null=True)
########## MODEL MOUVEMENT POUR LA SACHERIE ##############
class Mouvement2(models.Model):
    id_mvt = models.AutoField(primary_key=True)
    statut_entree = models.IntegerField()
    statut_sortie = models.IntegerField(null=True, blank=True)
    date_sortie = models.DateTimeField(null=True, blank=True)
    date_entree = models.DateTimeField(null=True, blank=True)
        ########## INTEGRATION  DES POINTEUR ############
    pointeur_entree = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_entree2',
                                            null=True, blank=True)
    pointeur_sortie = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_sortie2',
                                            null=True, blank=True)
        ########## INTEGRATION  DES CAMIONS ############
    camion = models.ForeignKey('Camion', on_delete=models.CASCADE, related_name='mouvements2', null=True, blank=True)
        ###chauffeur
    chauffeur = models.ForeignKey('Chaffeur', on_delete=models.CASCADE, related_name='mouvements2', null=True,
                                      blank=True)
        #####Mouvement0
        ###chauffeur
    id_mvt_0 = models.ForeignKey('Mouvement0', on_delete=models.CASCADE, related_name='mouvements2', null=True,
                                     blank=True)

    remorque = models.CharField(max_length=255, null=True)
    mission = models.CharField(max_length=255, null=True)

    def save(self, *args, **kwargs):
        if self.date_sortie and self.date_entree:
            self.duree = self.date_sortie - self.date_entree
        super().save(*args, **kwargs)
    def str(self):
        return f"Mouvement2 {self.id_mvt}"
#####UTILISATEUR #######
class Utilisateurs(models.Model):
    id_user = models.AutoField(primary_key=True, db_column='id_user')
    fullname = models.CharField(max_length=255)
    matricule = models.CharField(max_length=255,null=True)
    email = models.EmailField(unique=True,null=False)
    password = models.CharField(max_length=255,null=False)
    poste = models.CharField(max_length=255, null=False)
    status=models.CharField(max_length=255,default='active')
    def str(self):
        return f"Utilisateur {self.id_user}"
    ##################### USER #########################


class Chaffeur(models.Model):
    id_chauffeur = models.AutoField(primary_key=True, db_column='id_chauffeur')
    fullname = models.CharField(max_length=255)
    permis = models.CharField(max_length=255,null=True)
    telephone = models.CharField(max_length=255,null=True)
    def str(self):
        return f"Chaffeur {self.id_chauffeur}"

class Transitaire(models.Model):
    id_transit = models.AutoField(primary_key=True, db_column='id_transit')
    fullname = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    def str(self):
        return f"Transitaire {self.id_transit}"

class Mouvement0(models.Model):
    id_mvt = models.AutoField(primary_key=True)
    statut_entree = models.IntegerField()
    statut_sortie = models.IntegerField(null=True, blank=True)
    date_sortie = models.DateTimeField(null=True, blank=True)
    date_entree = models.DateTimeField(null=True, blank=True)
    ########## INTEGRATION  DES POINTEUR ############
    pointeur_entree = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_entree0', null=True, blank=True)
    pointeur_sortie = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_sortie0', null=True, blank=True)
    ########## INTEGRATION  DES CAMIONS ############
    camion = models.ForeignKey('Camion', on_delete=models.CASCADE, related_name='mouvements0', null=True, blank=True)
    ###chauffeur
    chauffeur = models.ForeignKey('Chaffeur', on_delete=models.CASCADE, related_name='mouvements0', null=True, blank=True)
    transitaire = models.ForeignKey('Transitaire', on_delete=models.CASCADE, related_name='mouvements0', null=True,
                                  blank=True)
    commentaire= models.ForeignKey('Commentaire', on_delete=models.CASCADE, related_name='mouvements0', null=True,
                                    blank=True)

    remorque = models.CharField(max_length=255,null=True)
    destination = models.CharField(max_length=255, null=True)


    def save(self, *args, **kwargs):
        if self.date_sortie and self.date_entree:
            self.duree = self.date_sortie - self.date_entree
        super().save(*args, **kwargs)
    def str(self):
        return f"Mouvement0 {self.id_mvt}"

class ParametrageDelais(models.Model):
    id_para = models.AutoField(primary_key=True, db_column='id_para')
    entite = models.CharField(max_length=255)
    nbr_max = models.CharField(max_length=255,null=True)
    type = models.CharField(max_length=20)
    delais_maximal = models.CharField(max_length=20)
    delais_urgent = models.CharField(max_length=20,null=True)

    def str(self):
        return f"ParametrageDelais {self.id_para}"
    ########################## MODEL MOUVMENT ZUD ############################
class Mouvement3(models.Model):
        id_mvt = models.AutoField(primary_key=True)
        statut_entree = models.IntegerField()
        statut_sortie = models.IntegerField(null=True, blank=True)
        date_sortie = models.DateTimeField(null=True, blank=True)
        date_entree = models.DateTimeField(null=True, blank=True)
        ########## INTEGRATION  DES POINTEUR ############
        pointeur_entree = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_entree3',
                                            null=True, blank=True)
        pointeur_sortie = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_sortie3',
                                            null=True, blank=True)
        ########## INTEGRATION  DES CAMIONS ############
        camion = models.ForeignKey('Camion', on_delete=models.CASCADE, related_name='mouvements3', null=True,
                                   blank=True)
        ###chauffeur
        chauffeur = models.ForeignKey('Chaffeur', on_delete=models.CASCADE, related_name='mouvements3', null=True,
                                      blank=True)
        #####Mouvement0
        ###chauffeur
        id_mvt_0 = models.ForeignKey('Mouvement0', on_delete=models.CASCADE, related_name='mouvements3', null=True,
                                     blank=True)

        remorque = models.CharField(max_length=255, null=True)
        mission = models.CharField(max_length=255, null=True)

        def save(self, *args, **kwargs):
            if self.date_sortie and self.date_entree:
                self.duree = self.date_sortie - self.date_entree
            super().save(*args, **kwargs)

        def str(self):
            return f"Mouvement3 {self.id_mvt}"

class Commentaire(models.Model):
    id_commentaire = models.AutoField(primary_key=True, db_column='id_commentaire')
    texte = models.CharField(max_length=255)

    def str(self):
        return f"Commentaire {self.id_commentaire}"

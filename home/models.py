from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
###################  Model  Commentaire  ####################

############Model CAMION #############
class Camion(models.Model):
    id_cam = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20)
    immatriculation = models.CharField(max_length=20)
    transporteur = models.TextField()
    def str(self):
        return f"Camion {self.id_cam} "
        ############Model Véhicule Particulier #############
class Vehicule(models.Model):
    id_veh = models.AutoField(primary_key=True)
    immatriculation = models.CharField(max_length=20)
    def str(self):
        return f"Camion {self.id_veh} "
############ MOUVEMENT MOUVMENT ICD TOM #############
class Mouvement1(models.Model):
    id_mvt = models.AutoField(primary_key=True)
    statut_entree = models.IntegerField(null=True, blank=True)
    statut_sortie = models.IntegerField(null=True, blank=True)
    date_sortie = models.DateTimeField(null=True, blank=True)
    date_entree = models.DateTimeField(null=True, blank=True)
    zone_entree = models.CharField(null=True, blank=True, max_length=55)
    zone_sortie = models.CharField(null=True, blank=True, max_length=55)
    ########## INTEGRATION  DES POINTEUR ############
    pointeur_entree = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_entree1', null=True, blank=True)
    pointeur_sortie = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_sortie1', null=True, blank=True)
    ########## INTEGRATION  DES CAMIONS ############
    camion = models.ForeignKey('Camion', on_delete=models.CASCADE, related_name='camionsNNmouvements1', null=True, blank=True)
    ###chauffeur
    chauffeur = models.ForeignKey('Chaffeur', on_delete=models.CASCADE, related_name='chauffeurmouvemeNNnts1', null=True, blank=True)
    #####CLIENT
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client1', null=True,
                               blank=True)
    ###MOUVMEENT0
    id_mvt_0 = models.ForeignKey('Mouvement0', on_delete=models.CASCADE, related_name='mouvements1', null=True,
                                  blank=True)
    remorque = models.CharField(max_length=255,null=True)
    mission = models.CharField(max_length=255, null=True)
######################## MODEL MOUVEMENT DE LA CMA ############################
class Mouvement4(models.Model):
    id_mvt = models.AutoField(primary_key=True)
    statut_entree = models.IntegerField(null=True, blank=True)
    statut_sortie = models.IntegerField(null=True, blank=True)
    date_sortie = models.DateTimeField(null=True, blank=True)
    date_entree = models.DateTimeField(null=True, blank=True)
    zone_entree = models.CharField(null=True, blank=True, max_length=55)
    zone_sortie = models.CharField(null=True, blank=True, max_length=55)
    ########## INTEGRATION  DES POINTEUR ############
    pointeur_entree = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_entree4', null=True, blank=True)
    pointeur_sortie = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_sortie4', null=True, blank=True)
    ########## INTEGRATION  DES CAMIONS ############
    camion = models.ForeignKey('Camion', on_delete=models.CASCADE, related_name='camionmouvements4', null=True, blank=True)
    ###chauffeur
    chauffeur = models.ForeignKey('Chaffeur', on_delete=models.CASCADE, related_name='chauffeurmouvements4', null=True, blank=True)
    #################Client
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client4', null=True,
                               blank=True)
    #####Mouvement0
    ###chauffeur
    id_mvt_0 = models.ForeignKey('Mouvement0', on_delete=models.CASCADE, related_name='mouvementsTY', null=True,
                                  blank=True)

    remorque = models.CharField(max_length=255,null=True)
    mission = models.CharField(max_length=255, null=True)
##############################MODEL MOUVEMENT DE EMSA ###################################
class Mouvement5(models.Model):
    id_mvt = models.AutoField(primary_key=True)
    statut_entree = models.IntegerField(null=True, blank=True)
    statut_sortie = models.IntegerField(null=True, blank=True)
    date_sortie = models.DateTimeField(null=True, blank=True)
    date_entree = models.DateTimeField(null=True, blank=True)
    zone_entree = models.CharField(null=True, blank=True, max_length=55)
    zone_sortie = models.CharField(null=True, blank=True, max_length=55)
    #################Client
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client5', null=True,
                               blank=True)
    ########## INTEGRATION  DES POINTEUR ############
    pointeur_entree = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements5_entree', null=True, blank=True)
    pointeur_sortie = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements5_sortie', null=True, blank=True)
    ########## INTEGRATION  DES CAMIONS ############
    camion = models.ForeignKey('Camion', on_delete=models.CASCADE, related_name='camionmouvements5', null=True, blank=True)
    ###chauffeur
    navire = models.CharField(max_length=255, null=True, blank=True)
    bl1 = models.CharField(max_length=255, null=True, blank=True)
    bl2 = models.CharField(max_length=255, null=True, blank=True)
    nbrcolis = models.IntegerField(null=True, blank=True)
    tonnage = models.IntegerField(null=True, blank=True)
    marchandise = models.CharField(max_length=255, null=True, blank=True)
    chauffeur = models.ForeignKey('Chaffeur', on_delete=models.CASCADE, related_name='chauffeurmouvementstyy', null=True, blank=True)
    #####Mouvement0
    ###chauffeur
    id_mvt_0 = models.ForeignKey('Mouvement0', on_delete=models.CASCADE, related_name='mouvementshggy', null=True,
                                  blank=True)

    remorque = models.CharField(max_length=255,null=True)
    mission = models.CharField(max_length=255, null=True)
########################### MODEL MOUVEMENT Mouvement de ITS ##################################
class Mouvement6(models.Model):
    id_mvt = models.AutoField(primary_key=True)
    statut_entree = models.IntegerField(null=True, blank=True)
    statut_sortie = models.IntegerField(null=True, blank=True)
    date_sortie = models.DateTimeField(null=True, blank=True)
    date_entree = models.DateTimeField(null=True, blank=True)
    zone_entree = models.CharField(null=True, blank=True, max_length=55)
    zone_sortie = models.CharField(null=True, blank=True, max_length=55)
    #################Client
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client6', null=True,
                               blank=True)

    ########## INTEGRATION  DES POINTEUR ############
    pointeur_entree = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements6_entree', null=True, blank=True)
    pointeur_sortie = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements6_sortie', null=True, blank=True)
    ########## INTEGRATION  DES CAMIONS ############
    navire = models.CharField(max_length=255, null=True, blank=True)
    bl1 = models.CharField(max_length=255, null=True, blank=True)
    bl2 = models.CharField(max_length=255, null=True, blank=True)
    poids = models.CharField(null=True, blank=True, max_length=255)
    poids_autorise = models.CharField(null=True, blank=True, max_length=255)
    pont_bascule = models.IntegerField(null=True, blank=True)
    destination = models.CharField(null=True, blank=True, max_length=255)
    nbrcolis = models.IntegerField(null=True, blank=True)
    tonnage = models.IntegerField(null=True, blank=True)
    marchandise = models.CharField(max_length=255, null=True, blank=True)
    camion = models.ForeignKey('Camion', on_delete=models.CASCADE, related_name='mouvements', null=True, blank=True)
    ###chauffeur
    chauffeur = models.ForeignKey('Chaffeur', on_delete=models.CASCADE, related_name='mouvementsgchghhgghghhghg', null=True, blank=True)
    #####Mouvement0
    ###chauffeur
    id_mvt_0 = models.ForeignKey('Mouvement0', on_delete=models.CASCADE, related_name='mouvementsggggff', null=True,
                                  blank=True)

    remorque = models.CharField(max_length=255,null=True)
    mission = models.CharField(max_length=255, null=True)
    ####################### MODEL MOUVEMENTS PARTICULIERS ############################
class Mouvement8(models.Model):
        id_mvt = models.AutoField(primary_key=True)
        date_sortie = models.DateTimeField(null=True, blank=True)
        date_entree = models.DateTimeField(null=True, blank=True)
        destination = models.CharField(null=True, blank=True)
        zone_entree = models.CharField(null=True, blank=True, max_length=55)
        zone_sortie = models.CharField(null=True, blank=True, max_length=55)
        ########## INTEGRATION  DES POINTEUR ############
        pointeur_entree = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements7_entreepart',
                                            null=True, blank=True)
        pointeur_sortie = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements7_sortiepart',
                                            null=True, blank=True)
        ########## INTEGRATION  DES CAMIONS ############
        vehicule = models.ForeignKey('Vehicule', on_delete=models.CASCADE, related_name='mouvementsgttyyy2partveh', null=True,
                                   blank=True)
        id_mvt_0 = models.ForeignKey('Mouvement0', on_delete=models.CASCADE, related_name='mouvementsGHGHGHpart', null=True,
                                     blank=True)
####################### MODEL MOUVEMENT POUR TRANSEXPRESS  ###########################
class Mouvement7(models.Model):
    id_mvt = models.AutoField(primary_key=True)
    statut_entree = models.IntegerField(null=True, blank=True)
    statut_sortie = models.IntegerField(null=True, blank=True)
    date_sortie = models.DateTimeField(null=True, blank=True)
    date_entree = models.DateTimeField(null=True, blank=True)
    zone_entree = models.CharField(null=True, blank=True, max_length=55)
    zone_sortie = models.CharField(null=True, blank=True, max_length=55)
    navire = models.CharField(max_length=255,null=True, blank=True)
    poids = models.CharField(null=True, blank=True, max_length=255)
    poids_autorise = models.CharField(null=True, blank=True, max_length=255)
    pont_bascule = models.IntegerField(null=True, blank=True)
    destination = models.CharField(null=True, blank=True, max_length=255)
    bl1 = models.CharField(max_length=255,null=True, blank=True)
    bl2 = models.CharField(max_length=255,null=True, blank=True)
    nbrcolis = models.IntegerField(null=True, blank=True)
    tonnage = models.IntegerField(null=True, blank=True)
    #################Client
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client7', null=True,
                               blank=True)
    marchandise = models.CharField(max_length=255,null=True, blank=True)
    ########## INTEGRATION  DES POINTEUR ############
    pointeur_entree = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements7_entree', null=True, blank=True)
    pointeur_sortie = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements7_sortie', null=True, blank=True)
    ########## INTEGRATION  DES CAMIONS ############
    camion = models.ForeignKey('Camion', on_delete=models.CASCADE, related_name='mouvementsgttyyy2', null=True, blank=True)
    ###chauffeur
    chauffeur = models.ForeignKey('Chaffeur', on_delete=models.CASCADE, related_name='mouvementsGJGGUGJ', null=True, blank=True)
    #####Mouvement0
    ###chauffeur
    id_mvt_0 = models.ForeignKey('Mouvement0', on_delete=models.CASCADE, related_name='mouvementsGHGHGH', null=True,
                                  blank=True)

    remorque = models.CharField(max_length=255,null=True)
    mission = models.CharField(max_length=255, null=True)
########## MODEL MOUVEMENT POUR LA SACHERIE ##############
class Mouvement2(models.Model):
    id_mvt = models.AutoField(primary_key=True)
    statut_entree = models.IntegerField(null=True, blank=True)
    statut_sortie = models.IntegerField(null=True, blank=True)
    date_sortie = models.DateTimeField(null=True, blank=True)
    date_entree = models.DateTimeField(null=True, blank=True)
    zone_entree = models.CharField(null=True, blank=True, max_length=55)
    zone_sortie = models.CharField(null=True, blank=True, max_length=55)
    poids = models.CharField(null=True, blank=True, max_length=255)
    poids_autorise = models.CharField(null=True, blank=True, max_length=255)
    pont_bascule = models.IntegerField(null=True, blank=True)
    destination = models.CharField(null=True, blank=True, max_length=255)
        ########## INTEGRATION  DES POINTEUR ############
    pointeur_entree = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements2_entree2',
                                            null=True, blank=True)
    pointeur_sortie = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements2_sortie2',
                                            null=True, blank=True)
        ########## INTEGRATION  DES CAMIONS ############
    camion = models.ForeignKey('Camion', on_delete=models.CASCADE, related_name='mouvements2GHGH', null=True, blank=True)
        ###chauffeur
    chauffeur = models.ForeignKey('Chaffeur', on_delete=models.CASCADE, related_name='mouvements2GJUGJG', null=True,
                                      blank=True)
       #################Client
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client2', null=True,
                                    blank=True)
        #####Mouvement0
    id_mvt_0 = models.ForeignKey('Mouvement0', on_delete=models.CASCADE, related_name='mouvements2GHGHGP', null=True,
                                     blank=True)
    code_camion =  models.CharField(null=True, blank=True)
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
    ##################### MODEL CHAUFFEUR #########################


class Chaffeur(models.Model):
    id_chauffeur = models.AutoField(primary_key=True, db_column='id_chauffeur')
    fullname = models.CharField(max_length=255)
    permis = models.CharField(max_length=255,null=True)
    telephone = models.CharField(max_length=255,null=True)
    date_exp_permis = models.DateField(null=True, blank=True)
    def str(self):
        return f"Chaffeur {self.id_chauffeur}"
###################### MODEL TRANSITAIRE ###########################
class Transitaire(models.Model):
    id_transit = models.AutoField(primary_key=True, db_column='id_transit')
    fullname = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    mission = models.CharField(max_length=255, null=True)
    def str(self):
        return f"Transitaire {self.id_transit}"
    ###################### MODEL CLIENT ########################
class Client(models.Model):
    id_client = models.AutoField(primary_key=True, db_column='id_client')
    fullname = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    def __str__(self):
        return f"Client {self.id_client}"
##################### MODEL MOUVEMENT DKLOG ##############################
class Mouvement0(models.Model):
    id_mvt = models.AutoField(primary_key=True)
    statut_entree = models.IntegerField(null=True, blank=True)
    statut_sortie = models.IntegerField(null=True, blank=True)
    date_sortie = models.DateTimeField(null=True, blank=True)
    date_entree = models.DateTimeField(null=True, blank=True)
    zone_entree = models.CharField(null=True, blank=True, max_length=55)
    zone_sortie = models.CharField(null=True, blank=True, max_length=55)
    mission = models.CharField(max_length=255, null=True)
    num_ticket = models.CharField(max_length=255, null=True)
    code_camion = models.CharField(null=True, blank=True)
    marchandise =   models.CharField(max_length=255,null=True)
    poids = models.CharField(null=True, blank=True, max_length=255)
    vehicule = models.ForeignKey('Vehicule', on_delete=models.CASCADE, related_name='modffsuvementsgttyyy2partveh',
                                 null=True,
                                 blank=True)
    ################### INTEGRATION DE TRANSITAIRE ET REPRESENTANT  ##############################
    transitaire = models.ForeignKey('Transitaire', on_delete=models.CASCADE, related_name='TransitaireMouvement0',
                                    null=True, blank=True)
    representant = models.ForeignKey('Transitaire', on_delete=models.CASCADE, related_name='RepresentantMouvement0',
                                     null=True, blank=True)
    poids_autorise = models.CharField(null=True, blank=True, max_length=255)
    pont_bascule = models.IntegerField(null=True, blank=True)
    destination = models.CharField(null=True, blank=True, max_length=255)
    destination_final = models.CharField(null=True, blank=True, max_length=255)
    numconteneur1 = models.CharField(max_length=255, null=True)
    typeconteneur1 = models.CharField(max_length=255, null=True)
    numconteneur2 = models.CharField(max_length=255, null=True)
    typeconteneur2 = models.CharField(max_length=255, null=True)
    numconteneur3 = models.CharField(max_length=255, null=True)
    typeconteneur3 = models.CharField(max_length=255, null=True)
    pregate = models.CharField(max_length=255,null=True)
    gatepass = models.CharField(max_length=255,null=True)
    navire = models.CharField(max_length=255, null=True, blank=True)
    bl1 = models.CharField(max_length=255, null=True, blank=True)
    bl2 = models.CharField(max_length=255, null=True, blank=True)
    date_validite = models.DateTimeField(null=True, blank=True)
    nbrcolis = models.IntegerField(null=True, blank=True)
    tonnage = models.IntegerField(null=True, blank=True)
    ########## INTEGRATION  DES POINTEUR ############
    pointeur_entree = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_entree0', null=True, blank=True)
    pointeur_sortie = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_sortie0', null=True, blank=True)
    ########## INTEGRATION  DES CAMIONS ############
    camion = models.ForeignKey('Camion', on_delete=models.CASCADE, related_name='mouvements0', null=True, blank=True)
    camionvrac = models.ForeignKey('Camion', on_delete=models.CASCADE, related_name='mouvements0vrac', null=True, blank=True)
    ###chauffeur
    chauffeur = models.ForeignKey('Chaffeur', on_delete=models.CASCADE, related_name='mouvements0', null=True, blank=True)
    transitaire = models.ForeignKey('Transitaire', on_delete=models.CASCADE, related_name='mouvements0', null=True,
                                  blank=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client0', null=True,
                                    blank=True, )
    remorque = models.CharField(max_length=255,null=True)
    destination = models.CharField(max_length=255, null=True)


    def save(self, *args, **kwargs):
        if self.date_sortie and self.date_entree:
            self.duree = self.date_sortie - self.date_entree
        super().save(*args, **kwargs)
    def str(self):
        return f"Mouvement0 {self.id_mvt}"
############################## MODEL PARAMETRE  #############################
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
        statut_entree = models.IntegerField(null=True, blank=True)
        statut_sortie = models.IntegerField(null=True, blank=True)
        date_sortie = models.DateTimeField(null=True, blank=True)
        date_entree = models.DateTimeField(null=True, blank=True)
        zone_entree = models.CharField(null=True, blank=True, max_length=55)
        zone_sortie = models.CharField(null=True, blank=True, max_length=55)
        num_ticket= models.CharField(max_length=255,null=True)
        ########## INTEGRATION  DES POINTEUR ############
        pointeur_entree = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_entree3',
                                            null=True, blank=True)
        pointeur_sortie = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE, related_name='mouvements_sortie3',
                                            null=True, blank=True)
        ################### INTEGRATION DE TRANSITAIRE ET REPRESENTANT  ##############################
        transitaire = models.ForeignKey('Transitaire', on_delete=models.CASCADE, related_name='TransitaireMouvement', null=True, blank=True)
        representant = models.ForeignKey('Transitaire', on_delete=models.CASCADE, related_name='RepresentantMouvement', null=True, blank=True)
        ########## INTEGRATION  DES CAMIONS ############
        camion = models.ForeignKey('Camion', on_delete=models.CASCADE, related_name='mouvements3', null=True,
                                   blank=True)
        ###chauffeur
        chauffeur = models.ForeignKey('Chaffeur', on_delete=models.CASCADE, related_name='mouvements3', null=True,
                                      blank=True)
        date_validite = models.DateTimeField(null=True, blank=True)
        marchandise = models.CharField(max_length=255, null=True)
        ################# CHAMPS CONCERNANT LES CONTENEURS #########################
        numconteneur1 = models.CharField(max_length=255, null=True)
        typeconteneur1 = models.CharField(max_length=255, null=True)
        numconteneur2 = models.CharField(max_length=255, null=True)
        typeconteneur2 = models.CharField(max_length=255, null=True)
        numconteneur3 = models.CharField(max_length=255, null=True)
        typeconteneur3 = models.CharField(max_length=255, null=True)
        pregate = models.CharField(max_length=255, null=True)
        gatepass = models.CharField(max_length=255, null=True)
        #####Client
        client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='client3', null=True,
                                        blank=True)
        ###Mouvement0
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
    ################ Model pour la table Réjet ################
class Rejet(models.Model):
    id_rejet = models.AutoField(primary_key=True)
    text = models.TextField()
    user = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
################ Model pour la table Observation ############
class Observation (models.Model):
    id_observation = models.AutoField(primary_key=True)
    user = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    bd = models.IntegerField(null=True, blank=True)
    dd = models.IntegerField(null=True, blank=True)
    enpanne = models.IntegerField(null=True, blank=True)
    motif_stationnement = models.CharField(null=True, blank=True)
    commentaire = models.CharField(null=True, blank=True, max_length=255)
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    id_mvt_0 = models.ForeignKey('Mouvement0', on_delete=models.CASCADE, related_name='mouvements3sdjhsdd', null=True,
                                 blank=True)
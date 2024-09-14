from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import *

urlpatterns = [
    path('index/<int:id>', views.index, name='index'),
    path('tables/', views.tables, name='tables'),
    path('detail_mvt/', views.detail_mvt, name='tables'),
    #####Gestion Camion
    path('liste_amion/<int:id>', liste_camion, name='listeCamion'),
    path('fetch_controlleur/', fetch_controlleur, name='fetch_controlleur'),
    path('fetch_observation/', fetch_observation, name='fetch_observation'),
    path('ajout_observation/', ajout_observation, name='ajout_observation'),
    ################# GESTION DES OBSERVATIONS #################################
    path('index_controller/<int:id>', index_controlleur, name='index_controller'),
    path('camion_zud/<int:id>', camion_zud, name='camion_zud'),
    ################### LOGIQUE RENDER OBSERVATION ##################################
    path('liste_observations/<int:id>', liste_observations, name='liste_observations'),
    ################### LOGIQUE RENDER OBSERVATION ADMIN ##################################
    path('liste_observationsadmin/<int:id>', liste_observationsadmin, name='liste_observationsadmin'),
    path('upload_exel/', importer_donnees_camion, name='signupc'),
    path('ajouter_camion_page/', ajouter_camion_page, name='listeCamion'),
    path('ajouter_camion/', ajouter_camion, name='listeCamion'),
    path('ajouter_vehicule_particulier/', ajouter_vehicule_particulier, name='listeCamion'),
    path('modifier_camion/', modifier_boite, name='listeCamionhhhhj'),
    #####Gestion Utilisateur
    path('liste_user/<int:id>', list_user, name='listeCamion'),
    path('upload_exel_user/', importer_donnees_utilisateur, name='signupc'),
    path('ajouter_camion_page/', ajouter_camion_page, name='listeCamion'),
    path('ajouter_user/', ajouter_user, name='listeCamion'),
    path('modifier_user/', modifier_user, name='listeCamionhhhhj'),
    #################Gestion Deatil
    # path('detail_urgent/<int:id>',detail_urgent, name='listeCamionud'),
    path('fect_urgent/<int:id>', mouvements_superieur_20_minutes, name='listeCamionud'),
    path('detail_urgent/<int:id>', detail_urgent, name='listeCamionud'),

    path('detail_depassement/<int:id>', detail_depassemnt, name='listeCamionud'),
    path('detail_plus_30/<int:id>', detail_plus_30, name='listeCamionud'),
    path('detail_moins_30/<int:id>', detail_moins_30, name='listeCamionud'),
    ###Gestion Connexion
    path('seconnecter/', seconnecter, name='seconnecter'),
    path('', login_page, name='login'),
    ######GESTION DES FETCH SUR LE DASHBOARD  ####################################
    ################### FETCH DASHBOARD PLT ###########################
    path('fetch_stats0/<int:id_user>/', fetch_stats0, name='fetch_stats0'),
    ################### FETCH DASHBOARD TOM ICD ###########################
    path('fetch_stats/<int:id_user>/', fetch_stats, name='fetch_stats'),
    ################### FETCH DASHBOARD CMA ICD ###########################
    path('fetch_stats1/<int:id_user>/', fetch_stats1, name='fetch_stats1'),
    ################### FETCH DASHBOARD SACHERIE  ###########################
    path('fetch_stats2/<int:id_user>/', fetch_stats2, name='fetch_stats2'),
    ############## FECH DASHBORD PLT
    # ################### FETCH DASHBOARD ZUD  ###########################
    path('fetch_stats3/<int:id_user>/', fetch_stats3, name='fetch_stats3'),
    path('fetch_statsparticulier/<int:id_user>/', fetch_statsparticulier, name='fetch_statsparticulier'),
    ############## FECH DASHBORD PLT
    path('index_dk_log0/<int:id>', views.index_dk0, name='index'),
    ################### GESTION DES FETCHS SUR LA LISTE DES MOLUVEMENTS DU DASHBOARD ###########
    ######################## PLT #####################################
    path('fetch_mouvementsdash0/', fetch_mouvementsdash0, name='fetch_mouvementsdash0'),
    ######################## ICD TOM  #####################################
    path('fetch_mouvementsdash/', fetch_mouvementsdash, name='fetch_mouvementsdash'),
    ######################## ICD CMA #####################################
    path('fetch_mouvementsdash1/', fetch_mouvementsdash1, name='fetch_mouvementsdash1'),
    ######################## SASHERIE #####################################
    path('fetch_mouvementsdash2/', fetch_mouvementsdash2, name='fetch_mouvementsdash2'),
    path('fetch_mouvementsdash3/', fetch_mouvementsdash3, name='fetch_mouvementsdash3'),
    ######################## ZUD #####################################
    ######################## PARTICUILIER #######################
    path('fetch_mouvementsdashparticulier/', fetch_mouvementsdashparticulier, name='fetch_mouvementsdashparticulier'),

    #####Gestion Mvt
    ################# GESTION DES FETCHS SUR  LE DASHBOARD #########################
    path('liste_mouvements/<int:id_user>', liste_mouvements, name='liste_mouvements'),
    path('ajoutmouvement/<int:id_user>/', ajoutmouvement, name='ajoutmouvement'),
    path('index1_view/<int:id_user>/', index1_view, name='index1_view'),
    path('sortie_tom/<int:id_user>/', sortie_tom, name='sortie_tom'),
    ######Gestion Sortie
    path('liste_mouvements1/<int:id_user>/', liste_mouvements1, name='liste_mouvements1'),
    path('liste_mouvementsdkparticulier/<int:id_user>/', liste_mouvementsdkparticulier,
         name='liste_mouvementsdkparticulier'),
    path('liste_mouvementsdk1/<int:id_user>/', liste_mouvementsdk1, name='liste_mouvementsdk1'),
    path('liste_mouvementsdk01/<int:id_user>/', liste_mouvementsdk01, name='liste_mouvementsdk01'),
    path('liste_mouvementsdk11/<int:id_user>/', liste_mouvementsdk11, name='liste_mouvementsdk11'),
    path('liste_mouvementsdk12/<int:id_user>/', liste_mouvementsdk12, name='liste_mouvementsdk12'),
    path('ajoutsortie', ajoutsortie, name='ajoutsortie'),
    path('ajoutsortiedk/', ajoutsortiedk, name='ajoutsortiedk'),
    path('ajoutsortiepar/', ajoutsortiepar, name='ajoutsortiepar'),
    path('liste_umvt/<int:id_mvt>', tout_mouvement, name='ajoutsortie'),
    ################### LISTE TOUS MOUVEMENT ADMINDKLOG PLT #######################"
    path('liste_tt_mvt00/<int:id_mvt>', tout_mouvement00, name='tout_tt_mouvement0'),
    ################### LISTE TOUS MOUVEMENT ADMINDKLOG ICD TOM #######################"
    path('liste_tt_mvt0/<int:id_mvt>', tout_mouvement0, name='tout_tt_mouvement0'),
    ################### LISTE TOUS MOUVEMENT ADMINDKLOG ICD CMA #######################"
    path('liste_tt_mvt01/<int:id_mvt>', tout_mouvement01, name='tout_tt_mouvement01'),
    ################### LISTE TOUS MOUVEMENT ADMINDKLOG SACHERIE #######################"
    path('liste_tt_mvt02/<int:id_mvt>', tout_mouvement02, name='tout_tt_mouvement02'),

    ################### LISTE TOUS MOUVEMENT ADMINDKLOG ZUD #######################"
    path('liste_tt_mvt03/<int:id_mvt>', tout_mouvement03, name='tout_tt_mouvement03'),
    path('liste_tt_mvt2/<int:id_mvt>', tout_mouvement2, name='tout_tt_mouvement2'),
    ###################### FETCH TOUT MOUVEMENT PLT #########################
    path('liste_mouvements_dk0/', liste_mouvements_dk0, name='liste_mouvements_dk0'),
    ###################### FETCH TOUT MOUVEMENT ICD TOM #########################
    path('liste_mouvements_dk/', liste_mouvements_dk, name='liste_mouvements_dk'),
    ###################### FETCH TOUT MOUVEMENT ICD CMA #########################
    path('liste_mouvements_dk1/', liste_mouvements_dk1, name='liste_mouvements_dk1'),
    ###################### FETCH TOUT MOUVEMENT SACHERIE #########################
    path('liste_mouvements_dk2/', liste_mouvements_dk2, name='liste_mouvements_dk2'),
    ###################### FETCH TOUT MOUVEMENT ZUD #########################
    path('liste_mouvements_dk3/', liste_mouvements_dk3, name='liste_mouvements_dk3'),
    path('liste_mouvements_sacherie/', liste_mouvements_sacherie, name='liste_mouvements_sacherie'),
    path('liste_mouvements2/', liste_mouvements2, name='liste_mouvements2'),
    path('modifier_mouvement/', modifier_mouvement, name='liste_mouvements2hfhfhgfhjj'),
    path('modifier_mouvement0/', modifier_mouvement0, name='liste_mouvements2hfhfhgfhjj0'),
    path('modifier_mouvement2/', modifier_mouvement2, name='liste_mouvements2hfhfhgfhjj2'),
    path('activer_desactiver_user/', activer_desactiver_user, name='liste_mouvements2hfhfhgfhfhfhgfhjgjjj'),
    path('deconnecter/', login_page, name='decon'),
    #############Gestion DEKALOG
    path('entreedecalog_particulier/<int:id_user>/', entreedecalog_particulier, name='entredecalog_particulier'),
    path('entreedecalog_view/<int:id_user>/', entredecalon_view, name='index1_view'),
    path('entreedecalog_view1/<int:id_user>/', entredecalon_view1, name='index1_view'),
    path('entreedecalog_view2/<int:id_user>/', entredecalon_view2, name='index1_view'),
    ################# FETCH POUR L'ICD #########################
    path('liste_mouvements0/', liste_mouvements_0, name='liste_mouvements0'),
    ###################### FETCH POUR LA SACHERIE
    path('liste_mouvements01/', liste_mouvements_01, name='liste_mouvements01'),
    #################### FETCH POUR LA ZUD ##################
    path('liste_mouvements02/', liste_mouvements_02, name='liste_mouvements02'),
    ####################### FETCH DE LA LISTE DES MOUVEMENTS PARTICULIERS #############
    path('liste_mouvementsparticulier/', liste_mouvements_particulier, name='liste_mouvements_particulier'),
    path('ajoutmouvement0/<int:id_user>/', ajoutmouvement0, name='ajoutmouvement0'),
    path('ajoutmouvementparticulier/<int:id_user>/', ajoutmouvementparticulier, name='ajoutmouvementparticulier'),
    path('entree_tom/', entree_tom, name='entree_tom'),

    path('entree_camion', entree_camion, name='entree_camion'),
    ################# SORTIE DKLOG PARTICULIER #########################
    path('sortie_decalog_viewparticulier/<int:id_user>/', sortie_decalog_viewparticulier,
         name='sortie_decalog_viewparticulier'),
    ################# SORTIE DKLOG ICD TOM #########################
    path('sortie_decalog_view/<int:id_user>/', sortie_decalog_view, name='sortie_decalog_view'),
    ################# SORTIE DKLOG ICD CMA #########################
    path('sortie_decalog_view01/<int:id_user>/', sortie_decalog_view01, name='sortie_decalog_view'),
    ################# SORTIE DKLOG SACHERIE #########################
    path('sortie_decalog_view1/<int:id_user>/', sortie_decalog_view1, name='sortie_decalog_view1'),
    ################# SORTIE DKLOG ZUD #########################
    path('sortie_decalog_view2/<int:id_user>/', sortie_decalog_view2, name='sortie_decalog_view2'),
    path('ajouter_camion_dk_log/', ajouter_camion_dk_log, name='listeCamion_dk_log'),
    path('ajouter_chauffeur/', ajouter_chauffeurs, name='ajouter_chauffeurs'),
    path('ajouter_client/', ajouter_client, name='ajouter_client'),
    path('ajouter_transitaire/', ajouter_transitaire, name='ajouter_transitaire'),
    path('fetch_camion/', fetch_camion, name='fetch_camion'),
    path('fetch_vehicule/', fetch_vehicule, name='fetch_vehicule'),
    path('fetch_camion_sacherie/', fetch_camion_sacherie, name='fetch_camion_sacherie'),
    path('fetch_chauffeur/', fetch_chauffeur, name='fetch_chauffeur'),
    path('fetch_transitaire/', fetch_transitaire, name='fetch_transitaire'),
    path('fetch_representant/', fetch_representant, name='fetch_representant'),
    path('fetch_representant/', fetch_representant, name='fetch_representant'),
    path('fetch_client/', fetch_client, name='fetch_client'),

    ######Gestion
    ################### SASHBOARD PLT ###########################
    path('index_dk_log0/<int:id>', views.index_dk0, name='index'),
    ################### SASHBOARD ICD TOM ###########################
    path('index_dk_log/<int:id>', views.index_dk, name='index'),
    ################### SASHBOARD ICD CMA ###########################
    path('index_dk_log1/<int:id>', views.index_dk1, name='index'),
    ################### SASHBOAD SACHERIE ###########################
    path('index_dk_log2/<int:id>', views.index_dk2, name='index'),
    ################### SASHBOAD ZUD ###########################
    path('index_dk_log3/<int:id>', views.index_dk3, name='index'),
    ################### SASHBOAD PARTICULIER ###########################
    path('index_dk_logparticulier/<int:id>', views.index_dkparticulier, name='indexparticulier'),
    ########################### INDEX ENTREE ICD TOM ################################
    path('index_entree_icdtom/<int:id_user>', index_entree_icdtom, name='index_entree_icdtom'),
    ########################### INDEX SORTIE ICD TOM ################################
    path('index_sortie_icdtom/<int:id_user>', index_sortie_icdtom, name='index_sortie_tom'),
    ########################### INDEX ENTREE ICD CMA ################################
    path('index_entree_icdcma/<int:id_user>', index_entree_icdcma, name='index_entree_icdcma'),
    ########################### INDEX SORTIE ICD CMA ################################
    path('index_sortie_icdcma/<int:id_user>', index_sortie_icdcma, name='index_sortie_cma'),
    #### INDEX POINTEURS ENTREE SACHERIE ############
    path('index2_view/<int:id>', index2_view, name='index2_view'),
    path('index3_view/<int:id>', index3_view, name='index3_view'),

    path('entree_sacherie', entree_sacherie, name='entree_sacherie'),
    # path('sortie_sacherie/<int:id_user>/',sortie_sacherie, name='sortie_sacherie'),
    path('liste_mouvements_3/<int:id_user>', liste_mouvements_3, name='liste_mouvements_3'),
    path('liste_mouvements4/<int:id_user>/', liste_mouvements4, name='liste_mouvements4'),
    path('ajoutsortie_sacherie', ajoutsortie_sacherie, name='ajoutsortie_sacherie'),
    path('index_sacherie/<int:id>', views.index_sacherie, name='index_sacherie'),
    ####detail sacherie

    path('detail_urgent_sacherie/<int:id>', detail_urgent_sacherie, name='detail_urgent_sacherie'),

    path('detail_depassement_sacherie/<int:id>', detail_depassement_sacherie, name='detail_depassement_sacherie'),
    path('detail_plus_30_sacherie/<int:id>', detail_plus_30_sacherie, name='detail_plus_30_sacherie'),
    path('detail_moins_30_sacherie/<int:id>', detail_moins_30_sacherie, name='detail_moins_30_sacherie'),

    ###################Detail DK LOG
    ####detail sacherie
    ############################### DETAIL URGENT PARTICULIER ####################################
    path('detail_urgent_dk_logpar/<int:id>', detail_urgent_dk_logpar, name='detail_urgent_dk_logpar'),
    ############################### DETAIL URGENT PLT ####################################
    path('detail_urgent_dk_log0/<int:id>', detail_urgent_dk_log0, name='detail_urgent_dk_log0'),
    ############################### DETAIL URGENT ICD TOM ####################################
    path('detail_urgent_dk_log/<int:id>', detail_urgent_dk_log, name='detail_urgent_dk_log'),
    ############################### DETAIL URGENT ICD CMA ####################################
    path('detail_urgent_dk_log1/<int:id>', detail_urgent_dk_log1, name='detail_urgent_dk_log1'),
    ############################### DETAIL URGENT SACHERIE  ####################################
    path('detail_urgent_dk_log2/<int:id>', detail_urgent_dk_log2, name='detail_urgent_dk_log2'),
    ############################### DETAIL URGENT ZUD  ####################################
    path('detail_urgent_dk_log/3<int:id>', detail_urgent_dk_log3, name='detail_urgent_dk_log3'),
    ############################### DETAIL DEPASSEMENT PARTICULIER ####################################
    path('detail_depassement_dk_logpar/<int:id>', detail_depassement_dk_logpar, name='detail_depassement_dk_logpar'),
    ############################### DETAIL DEPASSEMENT PLT ####################################
    path('detail_depassement_dk_log0/<int:id>', detail_depassement_dk_log0, name='detail_depassement_dk_log0'),
    ############################### DETAIL DEPASSEMENT ICD TOM ####################################
    path('detail_depassement_dk_log/<int:id>', detail_depassement_dk_log, name='detail_depassement_dk_log'),
    ############################### DETAIL DEPASSEMENT ICD CMA ####################################
    path('detail_depassement_dk_log1/<int:id>', detail_depassement_dk_log1, name='detail_depassement_dk_log1'),
    ############################### DETAIL DEPASSEMENT SACHERIE ####################################
    path('detail_depassement_dk_log2/<int:id>', detail_depassement_dk_log2, name='detail_depassement_dk_log2'),
    ############################### DETAIL DEPASSEMENT ZUD ####################################
    path('detail_depassement_dk_log3/<int:id>', detail_depassement_dk_log3, name='detail_depassement_dk_log3'),
    ####################### DETAILS PLUS DE 30 MINUTES PLT  #########################
    path('detail_plus_30_dk_log0/<int:id>', detail_plus_30_dk_log0, name='detail_plus_30_dk_log0'),
    ####################### DETAILS PLUS DE 30 MINUTES ICD TOM  #########################
    path('detail_plus_30_dk_log/<int:id>', detail_plus_30_dk_log, name='detail_plus_30_dk_log'),
    ####################### DETAILS PLUS DE 30 MINUTES ICD CMA#########################
    path('detail_plus_30_dk_log1/<int:id>', detail_plus_30_dk_log1, name='detail_plus_30_dk_log1'),
    ####################### DETAILS PLUS DE 30 MINUTES SACHERIE #########################
    path('detail_plus_30_dk_log2/<int:id>', detail_plus_30_dk_log2, name='detail_plus_30_dk_log2'),
    ####################### DETAILS PLUS DE 30 MINUTES ZUD  #########################
    path('detail_plus_30_dk_log3/<int:id>', detail_plus_30_dk_log3, name='detail_plus_30_dk_log3'),
    ################# DETAILS PLUS DE 30 MINUTES PARTICULIER  #########################
    path('detail_plus_30_dk_logpar/<int:id>', detail_plus_30_dk_logpar, name='detail_plus_30_dk_logpar'),
    ####################### DETAILS MOIS DE 30 MINUTES DKLOG PARTICULIER ################################
    path('detail_moins_30_dk_logpar/<int:id>', detail_moins_30_dk_logpar, name='detail_moins_30_dk_logpar'),
    ####################### DETAILS MOIS DE 30 MINUTES DKLOG PLT ################################
    path('detail_moins_30_dk_log0/<int:id>', detail_moins_30_dk_log0, name='detail_moins_30_dk_log0'),
    ####################### DETAILS MOIS DE 30 MINUTES DKLOG ICD TOM ################################
    path('detail_moins_30_dk_log/<int:id>', detail_moins_30_dk_log, name='detail_moins_30_dk_log'),

    ####################### DETAILS MOIS DE 30 MINUTES DKLOG ICD CMA ################################
    path('detail_moins_30_dk_log1/<int:id>', detail_moins_30_dk_log1, name='detail_moins_30_dk_log1'),
    ####################### DETAILS MOIS DE 30 MINUTES DKLOG SACHERIE ################################
    path('detail_moins_30_dk_log2/<int:id>', detail_moins_30_dk_log2, name='detail_moins_30_dk_log2'),
    ####################### DETAILS MOIS DE 30 MINUTES DKLOG  ZUD ################################
    path('detail_moins_30_dk_log3/<int:id>', detail_moins_30_dk_log3, name='detail_moins_30_dk_log3'),
    ######Extraction
    path('export_camions/', views.export_camions, name='export_camions'),
    path('export_mouvement0/', views.export_mouvement0, name='export_mouvement0'),
    path('export_mouvement2/', views.export_mouvement2, name='export_mouvement2'),
    path('export_mouvement1/', views.export_mouvement1, name='export_mouvement1'),
    ###Parametrage
    path('parametrage/<int:id>', liste_parametrage, name='listeParametrage'),
    path('ajouter_parametre/', ajouter_parametre, name='ajout_parametre'),
    path('modifier_parametre/', modifier_parametre, name='modifierparametre'),
    ################################### REDIRECTION ZUD #############################
    path('index_entree_zud/<int:id>', index_entree_zud, name='index_entree_zud'),
    path('index_sortie_zud/<int:id>', index_sortie_zud, name='index_sortie_zud'),
    path('index_admin_zud/<int:id>', index_admin_zud, name='index_admin_zud'),
    path('liste_mouvements_entree_zud/<int:id_user>', liste_mouvements_entree_zud, name='liste_mouvements_entree_zud'),
    path('liste_mouvements_sortie_zud/<int:id_user>', liste_mouvements_sortie_zud, name='liste_mouvements_sortie_zud'),
    path('entree_zud', entree_zud, name='entree_zud'),
    path('sortie_zud', sortie_zud, name='sortie_zud'),
    ####detail ZUD
    path('liste_mvt_zud/<int:id_mvt>', tout_mouvement_zud, name='tout_mouvement_zud'),

    path('detail_urgent_zud/<int:id>', detail_urgent_zud, name='detail_urgent_zud'),

    path('detail_depassement_zud/<int:id>', detail_depassement_zud, name='detail_depassement_zud'),
    path('detail_plus_30_zud/<int:id>', detail_plus_30_zud, name='detail_plus_30_zud'),
    path('detail_moins_30_zud/<int:id>', detail_moins_30_zud, name='detail_moins_30_zud'),
    path('liste_mouvements_suz/', liste_mouvements_zud, name='liste_mouvements_zud'),
    ######Extraction
    path('export_mouvement4/', views.export_mouvement4, name='export_mouvement4'),
    path('modifier_mouvement4/', modifier_mouvement4, name='liste_mouvements2hfhfhgfhjj4'),
    ###################### MODIFICATIONS DES MOUVEMENTS #############################
    ################# ICD ######################
    path('modif_mvt/<int:id_user>', modif_mvt, name='modif_mvt'),
    ################# SACHERIE ######################
    path('modif_mvt1/<int:id_user>', modif_mvt1, name='modif_mvt1'),
    ################# ZUD ######################
    path('modif_mvt2/<int:id_user>', modif_mvt2, name='modif_mvt2'),
    ############################## PARTICULIER #############################
path('modif_mvtpar/<int:id_user>', modif_mvtpar, name='modif_mvtpar'),
    ######################## FETCH DE LA LISTE DES MOUVEMENTS MODIFICATIONS ##########
    ############## ICD ###############
    path('liste_modifs/', liste_modifs, name='liste_modifs'),
    ############## SACHERIE ###############
    path('liste_modifs1/', liste_modifs1, name='liste_modifs1'),
    ############## ZUD  ###############
    path('liste_modifs2/', liste_modifs2, name='liste_modifs2'),
    path('liste_modifspar/', liste_modifspar, name='liste_modifspar'),
    ######################## LISTE MOUVEMENTS ENTREE CMA ######################
    path('liste_mouvements_entree_cma/<int:id_user>', liste_mouvements_entree_cma, name='liste_mouvements_entree_cma'),
    ######################## LISTE MOUVEMENTS SORTIE CMA ####################################
    path('liste_mouvements_sortie_cma/<int:id_user>', liste_mouvements_sortie_cma, name='liste_mouvements_sortie_cma'),
]

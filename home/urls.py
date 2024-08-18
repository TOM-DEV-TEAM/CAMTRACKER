from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import *

urlpatterns = [
  path('index/<int:id>', views.index,  name='index'),
  path('tables/', views.tables, name='tables'),
  path('detail_mvt/', views.detail_mvt, name='tables'),
  #####Gestion Camion
  path('liste_amion/<int:id>', liste_camion, name='listeCamion'),
  path('upload_exel/', importer_donnees_camion, name='signupc'),
  path('ajouter_camion_page/', ajouter_camion_page, name='listeCamion'),
  path('ajouter_camion/', ajouter_camion, name='listeCamion'),
  path('modifier_camion/', modifier_boite, name='listeCamionhhhhj'),
  #####Gestion Utilisateur
path('liste_user/<int:id>',list_user, name='listeCamion'),
  path('upload_exel_user/', importer_donnees_utilisateur, name='signupc'),
  path('ajouter_camion_page/', ajouter_camion_page, name='listeCamion'),
  path('ajouter_user/', ajouter_user, name='listeCamion'),
  path('modifier_user/', modifier_user, name='listeCamionhhhhj'),
  #################Gestion Deatil
  #path('detail_urgent/<int:id>',detail_urgent, name='listeCamionud'),
  path('fect_urgent/<int:id>',mouvements_superieur_20_minutes, name='listeCamionud'),
path('detail_urgent/<int:id>',detail_urgent, name='listeCamionud'),

  path('detail_depassement/<int:id>',detail_depassemnt, name='listeCamionud'),
  path('detail_plus_30/<int:id>',detail_plus_30, name='listeCamionud'),
  path('detail_moins_30/<int:id>',detail_moins_30, name='listeCamionud'),
  ###Gestion Connexion
    path('seconnecter/', seconnecter, name='seconnecter'),
    path('', login_page, name='login'),
  #####Gestion Mvt
  path('liste_mouvements/<int:id_user>', liste_mouvements, name='liste_mouvements'),
  path('ajoutmouvement/<int:id_user>/',ajoutmouvement, name='ajoutmouvement'),
  path('index1_view/<int:id_user>/',index1_view, name='index1_view'),
  path('sortie_tom/<int:id_user>/', sortie_tom ,name='sortie_tom'),
  ######Gestion Sortie
   path('liste_mouvements1/<int:id_user>/', liste_mouvements1, name='liste_mouvements1'),
  path('liste_mouvementsdk1/<int:id_user>/', liste_mouvementsdk1, name='liste_mouvementsdk1'),
   path('ajoutsortie',ajoutsortie, name='ajoutsortie'),
  path('ajoutsortiedk/',ajoutsortiedk, name='ajoutsortiedk'),
   path('liste_umvt/<int:id_mvt>',tout_mouvement, name='ajoutsortie'),
  path('liste_tt_mvt0/<int:id_mvt>',tout_mouvement0, name='tout_tt_mouvement0'),
  path('liste_tt_mvt2/<int:id_mvt>',tout_mouvement2, name='tout_tt_mouvement2'),
path('liste_mouvements_dk/', liste_mouvements_dk, name='liste_mouvements_dk'),
path('liste_mouvements_sacherie/', liste_mouvements_sacherie, name='liste_mouvements_sacherie'),
   path('liste_mouvements2/', liste_mouvements2, name='liste_mouvements2'),
  path('modifier_mouvement/', modifier_mouvement, name='liste_mouvements2hfhfhgfhjj'),
path('modifier_mouvement0/', modifier_mouvement0, name='liste_mouvements2hfhfhgfhjj0'),
path('modifier_mouvement2/', modifier_mouvement2, name='liste_mouvements2hfhfhgfhjj2'),
  path('activer_desactiver_user/', activer_desactiver_user, name='liste_mouvements2hfhfhgfhfhfhgfhjgjjj'),
  path('deconnecter/', login_page, name='decon'),
  #############Gestion DEKALOG
  path('entreedecalog_view/<int:id_user>/',entredecalon_view, name='index1_view'),

  path('liste_mouvements0/', liste_mouvements_0, name='liste_mouvements0'),
  path('ajoutmouvement0/<int:id_user>/',ajoutmouvement0, name='ajoutmouvement0'),
  path('entree_tom/',entree_tom, name='entree_tom'),

path('entree_camion',entree_camion, name='entree_camion'),
  path('sortie_decalog_view/<int:id_user>/', sortie_decalog_view, name='sortie_decalog_view'),
  path('ajouter_camion_dk_log/', ajouter_camion_dk_log, name='listeCamion_dk_log'),
  path('ajouter_chauffeur/', ajouter_chauffeur, name='ajouter_chauffeur'),
    path('ajouter_transitaire/', ajouter_transitaire, name='ajouter_transitaire'),
  path('fetch_camion/', fetch_camion, name='fetch_camion'),
path('fetch_chauffeur/', fetch_chauffeur, name='fetch_chauffeur'),
  ######Gestion
path('index_dk_log/<int:id>', views.index_dk,  name='index'),
  #####Gestion Sacherie
  path('index2_view/<int:id>', index2_view,  name='index2_view'),
path('index3_view/<int:id>', index3_view,  name='index3_view'),

  path('entree_sacherie',entree_sacherie, name='entree_sacherie'),
  #path('sortie_sacherie/<int:id_user>/',sortie_sacherie, name='sortie_sacherie'),
  path('liste_mouvements_3/<int:id_user>', liste_mouvements_3, name='liste_mouvements_3'),
  path('liste_mouvements4/<int:id_user>/', liste_mouvements4, name='liste_mouvements4'),
  path('ajoutsortie_sacherie',ajoutsortie_sacherie, name='ajoutsortie_sacherie'),
  path('index_sacherie/<int:id>', views.index_sacherie,  name='index_sacherie'),
  ####detail sacherie

 path('detail_urgent_sacherie/<int:id>',detail_urgent_sacherie, name='detail_urgent_sacherie'),

  path('detail_depassement_sacherie/<int:id>',detail_depassement_sacherie, name='detail_depassement_sacherie'),
  path('detail_plus_30_sacherie/<int:id>',detail_plus_30_sacherie, name='detail_plus_30_sacherie'),
  path('detail_moins_30_sacherie/<int:id>',detail_moins_30_sacherie, name='detail_moins_30_sacherie'),

###################Detail DK LOG
####detail sacherie

 path('detail_urgent_dk_log/<int:id>',detail_urgent_dk_log, name='detail_urgent_dk_log'),

  path('detail_depassement_dk_log/<int:id>',detail_depassement_dk_log, name='detail_depassement_dk_log'),
  path('detail_plus_30_dk_log/<int:id>',detail_plus_30_dk_log, name='detail_plus_30_dk_log'),
  path('detail_moins_30_dk_log/<int:id>',detail_moins_30_dk_log, name='detail_moins_30_dk_log'),
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
path('entree_zud',entree_zud, name='entree_zud'),
    path('sortie_zud', sortie_zud, name='sortie_zud'),
####detail ZUD
path('liste_mvt_zud/<int:id_mvt>',tout_mouvement_zud, name='tout_mouvement_zud'),

 path('detail_urgent_zud/<int:id>',detail_urgent_zud, name='detail_urgent_zud'),

  path('detail_depassement_zud/<int:id>',detail_depassement_zud, name='detail_depassement_zud'),
  path('detail_plus_30_zud/<int:id>',detail_plus_30_zud, name='detail_plus_30_zud'),
  path('detail_moins_30_zud/<int:id>',detail_moins_30_zud, name='detail_moins_30_zud'),
    path('liste_mouvements_suz/', liste_mouvements_zud, name='liste_mouvements_zud'),
    ######Extraction
path('export_mouvement4/', views.export_mouvement4, name='export_mouvement4'),
path('modifier_mouvement4/', modifier_mouvement4, name='liste_mouvements2hfhfhgfhjj4'),
]
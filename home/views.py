import math
from audioop import reverse

from django.db.models import Q
from django.utils import timezone
from urllib import request

import pandas as pd
from admin_datta.utils import JsonResponse
from django.db import transaction
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.contrib.auth import logout, authenticate, login

from django.contrib.auth.decorators import login_required
from datetime import timedelta, datetime
from django.utils import timezone
from openpyxl.workbook import Workbook

from .models import Mouvement1

from .forms import MouvementForm, SortieForm, ChauffeurForm, CamionForm
from .models import *

def index(request,id):
    #paratom=ParametrageDelais.
    vingt_minutes = timedelta(minutes=20)
    trt_minutes = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements = Mouvement1.objects.filter(date_entree__isnull=False,date_sortie__isnull=True)
    mouvements_filtrés = [mvt for mvt in mouvements if (maintenant - mvt.date_entree) >= vingt_minutes and (
                maintenant - mvt.date_entree) < trt_minutes]
    urg = len(mouvements_filtrés)
   ###Depassement

    mouvements_dep = Mouvement1.objects.filter(date_entree__isnull=False,date_sortie__isnull=True)
    mouvements_filtrés_dep = [mvt for mvt in mouvements_dep if (maintenant - mvt.date_entree) >= trt_minutes]
    dep = len(mouvements_filtrés_dep)

    ###Plus 30
    vingt_minutes_30 = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements_30 = Mouvement1.objects.filter(date_entree__isnull=False,date_sortie__isnull=False)
    mouvements_filtrés_30 = [mvt for mvt in mouvements_30 if (mvt.date_sortie - mvt.date_entree) >= trt_minutes]
    lg_30 = len(mouvements_filtrés_30)
    #####OIMS 30

    vingt_minutes_moin = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements_moins = Mouvement1.objects.filter(date_entree__isnull=False,date_sortie__isnull=False)
    mouvements_filtrés_moins = [mvt for mvt in mouvements_moins if
                                (mvt.date_sortie - mvt.date_entree) < trt_minutes]
    lg_moins = len(mouvements_filtrés_moins)
    mvt_total=Mouvement1.objects.filter(date_entree__isnull=False,date_sortie__isnull=True)
    total_cours =len(mvt_total)
    totalter = lg_30 + lg_moins
    tout_mouvements= Mouvement1.objects.filter(date_entree__isnull=False,date_sortie__isnull=True)[:5]
    vingt_minutes = timedelta(minutes=30)
    trt = timedelta(minutes=20)


    for mvt in tout_mouvements :
        diff = (maintenant - mvt.date_entree).total_seconds()/60
        mvt.chrono=int(diff)

        #duree=math.ceil((mvt.date_sortie - mvt.date_entree).total_seconds() / 3600)
        duree=float(diff)
        if duree >=30 :
            mvt.etat= 3
        if duree <30 and duree > 20 :
            mvt.etat= 2
        if duree <= 20 :
          mvt.etat= 1

        camion=Camion.objects.get(id_cam=mvt.camion_id)
        mvt.cam=camion.immatriculation
    user=Utilisateurs.objects.get(id_user=id)
    return render(request, 'pages/index.html',
                  { 'urg': urg, 'dep': dep, 'lg_30': lg_30, 'lg_mois': lg_moins,
                   'total_cours': total_cours, 'total_ter': totalter,'mvt':tout_mouvements,'util' :user})

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)

def detail_mvt(request):
  context = {
    'segment': 'index',
    # 'products' : Product.objects.all()
  }
  return render(request, "pages/detail.html", context)

def tout_mvt(request):
  tout_mvt=Mouvement1.objects.all()
  ids_camion = set(tout_mvt.values_list('camion_id', flat=True))
  ids_point = set(tout_mvt.values_list('camion_id', flat=True))

  # Ajouter dynamiquement l'attribut 'acces=0' aux documents restreints dans listedoc
  data = []
  for doc in tout_mvt:
    camion=Camion.objects.get(id_cam=doc.camion_id)
    doc.id_cam=camion.id_cam
    doc.immat=camion.immatriculation
    doc.ttrans=camion.transporteur
    ptr_etr=Utilisateurs.objects.get(id_user=doc.pointeur_entree)
    doc.ptr_etr= ptr_etr.nom + ptr_etr.prenom
    if doc.pointeur_sortie :
      ptr_srt = Utilisateurs.objects.get(id_user=doc.pointeur_entree)
      doc.ptr_srt = ptr_srt.nom + ptr_srt.prenom
    else:
      doc.ptr_srt = 'Auncun'

  context = {
    'segment': 'index',
    'mvt' : tout_mvt
    # 'products' : Product.objects.all()
  }
  return render(request, "pages/detail.html", context)





def mvt_termine(request):
  tout_mvt_crs=Mouvement1.objects.filter(date_sortie__isnull=False)
  ids_camion = set(tout_mvt.values_list('camion_id', flat=True))
  ids_point = set(tout_mvt.values_list('camion_id', flat=True))
  ids_camion = set(tout_mvt.values_list('camion_id', flat=True))
  ids_point = set(tout_mvt.values_list('camion_id', flat=True))

  # Ajouter dynamiquement l'attribut 'acces=0' aux documents restreints dans listedoc
  data = []
  moins_de_30_minutes = []
  plus_de_30_minutes = []
  for doc in tout_mvt:
    camion=Camion.objects.get(id_cam=doc.camion_id)
    doc.id_cam=camion.id_cam
    doc.immat=camion.immatriculation
    doc.ttrans=camion.transporteur
    ptr_etr=Utilisateurs.objects.get(id_user=doc.pointeur_entree)
    doc.ptr_etr= ptr_etr.nom + ptr_etr.prenom
    ptr_srt = Utilisateurs.objects.get(id_user=doc.pointeur_entree)
    doc.ptr_srt = ptr_srt.nom + ptr_srt.prenom
    duree= (doc.date_sortie - doc.date_entree)/60
    if duree <= 30:
      moins_de_30_minutes.append(doc)
    else:
      plus_de_30_minutes.append(doc)

  context = {
    'segment': 'index',
    'mvt' : tout_mvt,
    'moins': moins_de_30_minutes,
    'plus': plus_de_30_minutes
    # 'products' : Product.objects.all()
  }
  return render(request, "pages/detail.html", context)

def mvt_termine(request):
  tout_mvt_crs=Mouvement1.objects.filter(date_sortie__isnull=True)
  ids_camion = set(tout_mvt.values_list('camion_id', flat=True))
  ids_point = set(tout_mvt.values_list('camion_id', flat=True))
  ids_camion = set(tout_mvt.values_list('camion_id', flat=True))
  ids_point = set(tout_mvt.values_list('camion_id', flat=True))

  # Ajouter dynamiquement l'attribut 'acces=0' aux documents restreints dans listedoc
  data = []
  moins_de_30_minutes = []
  plus_de_30_minutes = []
  for doc in tout_mvt:
    camion=Camion.objects.get(id_cam=doc.camion_id)
    doc.id_cam=camion.id_cam
    doc.immat=camion.immatriculation
    doc.ttrans=camion.transporteur
    ptr_etr=Utilisateurs.objects.get(id_user=doc.pointeur_entree)
    doc.ptr_etr= ptr_etr.nom + ptr_etr.prenom
    ptr_srt = Utilisateurs.objects.get(id_user=doc.pointeur_entree)
    doc.ptr_srt = ptr_srt.nom + ptr_srt.prenom
    now = timezone.now()  # Obtenir la date et l'heure actuelles
    difference = now - doc.date_entree
    duree=difference.total_seconds() / 60
    if duree <= 30:
      moins_de_30_minutes.append(doc)
    else:
      plus_de_30_minutes.append(doc)

  context = {
    'segment': 'index',
    'mvt' : tout_mvt,
    'moins':moins_de_30_minutes,
    'plus' :plus_de_30_minutes
    # 'products' : Product.objects.all()
  }
  return render(request, "pages/detail.html", context)


def fetch_mvt_termine(request):
  tout_mvt_crs=Mouvement1.objects.filter(date_sortie__isnull=False)
  ids_camion = set(tout_mvt.values_list('camion_id', flat=True))
  ids_point = set(tout_mvt.values_list('camion_id', flat=True))
  ids_camion = set(tout_mvt.values_list('camion_id', flat=True))
  ids_point = set(tout_mvt.values_list('camion_id', flat=True))

  # Ajouter dynamiquement l'attribut 'acces=0' aux documents restreints dans listedoc
  data = []
  moins_de_30_minutes = []
  plus_de_30_minutes = []
  for doc in tout_mvt:
    camion=Camion.objects.get(id_cam=doc.camion_id)
    doc.id_cam=camion.id_cam
    doc.immat=camion.immatriculation
    doc.ttrans=camion.transporteur
    ptr_etr=Utilisateurs.objects.get(id_user=doc.pointeur_entree)
    doc.ptr_etr= ptr_etr.nom + ptr_etr.prenom
    ptr_srt = Utilisateurs.objects.get(id_user=doc.pointeur_entree)
    doc.ptr_srt = ptr_srt.nom + ptr_srt.prenom
    duree= (doc.date_sortie - doc.date_entree)/60
    if duree <= 30:
      moins_de_30_minutes.append(doc)
    else:
      plus_de_30_minutes.append(doc)

  context = {
    'segment': 'index',
    'mvt' : tout_mvt,
    'moins': moins_de_30_minutes,
    'plus': plus_de_30_minutes
    # 'products' : Product.objects.all()
  }
  return render(request, "pages/detail.html", context)






######Gestion Camion
########################################AGENT#######################################################
def liste_camion(request, id):
 listeboite=Camion.objects.all()
 user=Utilisateurs.objects.get(id_user=id)
 #user=2
 return render(request, 'pages/gestion_camion.html', {'boite': listeboite,'util': user})
#####Gestion User

 def Crer_agent_page(request, id):
   # forms = UtilisateurForm(request.POST)
   user = UtilisateursTraking.objects.get(id_utilisateur=id)
   # return render(request, 'templatetra/crer_agent.html', {'forms': forms, 'util': user})
   return render(request, 'templatetra/crer_agent.html', {'util': user})


def enregistrer_agent(request):
  if request.method == 'POST':
    # form = UtilisateuwrForm(request.POST)
    form = 1
    user = UtilisateursTraking.objects.get(id_utilisateur=request.POST["id_user"])
    if form.is_valid() or 1:
      cleaned_data = form.cleaned_data
      instance = UtilisateursTraking(
        nom=request.POST['nom'],
        prenom=request.POST['prenom'],
        email=request.POST['email'],
        password='passer',
        telephone=request.POST['telephone'],
        role=request.POST['rolee']

        # form.cleaned_data['direction']
      )
      instance.save()
      # return redirect('/users/login/')
      return list_agent(request, user.id_utilisateur)
    else:
      # forms = UtilisateurForm()
      return Crer_agent_page(request, request.POST["id_user"])
      # return render(request, 'templatetra/crer_agent.html', {'forms': forms})


def update_agent_page(request, id_user, id_agt):
  user = UtilisateursTraking.objects.get(id_utilisateur=id_user)
  agt = UtilisateursTraking.objects.get(id_utilisateur=id_agt)
  return render(request, 'templatetra/update_agent.html', {'agt': agt, 'util': user, 'user': agt})


def upadte_agent(request):
  agt = UtilisateursTraking.objects.get(id_utilisateur=request.POST['id_agt'])
  user = UtilisateursTraking.objects.get(id_utilisateur=request.POST['id_user'])
  if request.POST['prenom']:
    agt.prenom = request.POST['prenom']
  if request.POST['nom']:
    agt.email = request.POST['nom']
  if request.POST['telephone']:
    agt.telephone = request.POST['telephone'],

  agt.save()
  return list_agent(request, user.id_utilisateur)


def desactiver_agent(request, id_user, id_agt):
  user = UtilisateursTraking.objects.get(id_utilisateur=id_user)
  agt = UtilisateursTraking.objects.get(id_utilisateur=id_agt)
  agt.etat = 0
  agt.save()
  return list_agent(request, user.id_utilisateur)


def activer_agent(request, id_user, id_agt):
  user = UtilisateursTraking.objects.get(id_utilisateur=id_user)
  agt = UtilisateursTraking.objects.get(id_utilisateur=id_agt)
  agt.etat = 1
  agt.save()
  return list_agent(request, user.id_utilisateur)


def reinitiliaser_mdp(request, id_user, id_agt):
  user = UtilisateursTraking.objects.get(id_utilisateur=id_user)
  agt = UtilisateursTraking.objects.get(id_utilisateur=id_agt)
  agt.password = 'reinit'
  agt.save()
  return list_agent(request, user.id_utilisateur)

##############Import Fichier Camion
@csrf_exempt
def importer_donnees_camion_excel(fichier_excel):
    """
    Importe les données d'un fichier Excel dans la table Camion.

    Args:
        fichier_excel (UploadedFile): Le fichier Excel à importer.

    Raises:
        ValueError: Si le fichier Excel n'est pas valide.
    """

    if not fichier_excel.content_type.startswith('application/vnd.openxmlformats'):
        raise ValueError('Le fichier Excel n\'est pas valide.')

    # Lire le fichier Excel dans un DataFrame Pandas
    df = pd.read_excel(fichier_excel)

    # Vérifier si les colonnes du DataFrame correspondent aux champs du modèle Camion
    champs_camion = ['immatriculation', 'transporteur','type']
    if not df.columns.isin(champs_camion).all():
        raise ValueError('Le fichier Excel ne contient pas les colonnes requises.')

    # Enregistrer les données dans la base de données
    with transaction.atomic():
        for index, row in df.iterrows():
            camion = Camion(
                immatriculation=row['immatriculation'],
                transporteur=row['transporteur'],
                type=row['type'],
            )
            camion.save()


@csrf_exempt
def importer_donnees_camion(request):
    if request.method == 'POST':
        fichier_excel = request.FILES['fichier_excel']
        try:
            importer_donnees_camion_excel(fichier_excel)
            message = 'Données importées avec succès.'
        except ValueError as e:
            message = e.args[0]
    else:
        fichier_excel = None
        message = ''
    #user=Utilisateurs.objects.get(poste='admin')
    user = Utilisateurs.objects.get(id_user=1)
    return  redirect("/liste_amion/" +str(user.id_user))


def ajouter_camion_page(request):
  return render(request, 'pages/ajouter_camion.html',)
@csrf_exempt

def ajouter_camion(request):
  if request.method == 'POST':
    #form = BoiteForm(request.POST)
    #id_user = request.session.get('user_id')
    if Camion.objects.filter(immatriculation=request.POST['imat']).exists():
      return redirect()
      # cleaned_data = form.cleaned_data
    else:
      camion = Camion(
        immatriculation=request.POST['imat'],
        transporteur=request.POST['trans'],
          type=request.POST['type'],
      )
      camion.save()

      return redirect("/liste_amion/" + str(request.POST['id_user']))

  else:

    # return ajouterboite_page(request, request.POST['id_user'])
    return redirect("/doc/jouterboite_page/" + str(request.POST['id_user']))

def modifier_boite(request):
    if request.method == 'POST':
      boite_id = request.POST['boite_id']
      boite = get_object_or_404(Camion, id_cam=boite_id)
      boite.immatriculation = request.POST['immat']
      boite.transporteur = request.POST['trans']
      boite.type = request.POST['type']
      boite.save()
      #return redirect(reverse('index'))  # Redirigez vers la page index après la modification
      return redirect("/liste_amion/" + str(request.POST['id_user']))

    return render(request, 'index.html')


#####Gestion Utilisateur

def list_user(request, id):
 listeboite=Utilisateurs.objects.all()
 user=Utilisateurs.objects.get(id_user=id)
 return render(request, 'pages/gestion_utilisateurs.html', {'boite': listeboite,'util' : user})

##############Import Fichier Camion
def importer_donnees_utilisateur_excel(fichier_excel):
    """
    Importe les données d'un fichier Excel dans la table Camion.

    Args:
        fichier_excel (UploadedFile): Le fichier Excel à importer.

    Raises:
        ValueError: Si le fichier Excel n'est pas valide.
    """

    if not fichier_excel.content_type.startswith('application/vnd.openxmlformats'):
        raise ValueError('Le fichier Excel n\'est pas valide.')

    # Lire le fichier Excel dans un DataFrame Pandas
    df = pd.read_excel(fichier_excel)

    # Vérifier si les colonnes du DataFrame correspondent aux champs du modèle Camion
    champs_camion = ['fullname', 'matricule', 'email', 'password', 'poste','statut']
    if not df.columns.isin(champs_camion).all():
        raise ValueError('Le fichier Excel ne contient pas les colonnes requises.')

    # Enregistrer les données dans la base de données
    with transaction.atomic():
        for index, row in df.iterrows():
            camion = Utilisateurs(
              fullname=row['fullname'],
                matricule=row['matricule'],
              email=row['email'],
              password=row['password'],
              poste=row['poste'],
                status=row['statut'],

            )
            camion.save()



def importer_donnees_utilisateur(request):
    if request.method == 'POST':
        fichier_excel = request.FILES['fichier_excel']
        try:
            importer_donnees_utilisateur_excel(fichier_excel)
            message = 'Données importées avec succès.'
        except ValueError as e:
            message = e.args[0]
    else:
        fichier_excel = None
        message = ''
    return  redirect("/liste_user/2")


def ajouter_utilisateur_page(request):
  return render(request, 'pages/ajouter_camion.html',)
@csrf_exempt
def ajouter_user(request):
  if request.method == 'POST':
    user = Utilisateurs.objects.get(id_user=request.POST['id_user'])
    if Utilisateurs.objects.filter(email=request.POST['email']).exists():
        return redirect("/liste_user/" + str(user.id_user))
    else:

      camion = Utilisateurs(
        #nom=request.POST['nom'],
        fullname=request.POST['prenom'],
        email=request.POST['email'],
          matricule=request.POST['matricule'],
        password=request.POST['password'],
        poste=request.POST['poste'],

      )
      camion.save()
  user=Utilisateurs.objects.get(id_user=request.POST['id_user'])

  return redirect("/liste_user/" + str(user.id_user))

  #else:

    # return ajouterboite_page(request, request.POST['id_user'])
    #return redirect("/doc/jouterboite_page/" + str(request.POST['id_user']))

def modifier_user(request):
    if request.method == 'POST':
      boite_id = request.POST['boite_id']
      boite = get_object_or_404(Utilisateurs, id_user=boite_id)
      #boite.nom = request.POST['nom']
      boite.fullname= request.POST['prenom']
      boite.email = request.POST['email']
      boite.password = request.POST['password']
      boite.poste = request.POST['poste']
      boite.save()
      #return redirect(reverse('index'))  # Redirigez vers la page index après la modification
      #user=Utilisateurs.objects.get(poste='superadmin')
      return redirect("/liste_user/" + str(request.POST['id_user']))
    return redirect("/liste_user/"+ str(request.POST['id_user']))


############Gestion Detail


def mouvements_superieur_20_minutes(request, id):
    vingt_minutes = timedelta(minutes=20)
    maintenant = timezone.now()
    mouvements = Mouvement1.objects.filter(date_sortie__isnull=True).values('id_mvt', 'camion_id', 'statut_entree', 'statut_sortie', 'chauffeur',
                                                'permis', 'remorque','date_entree','pointeur_entree_id')
    mouvements = list( mouvements)
    mouvements_filtrés = [mvt for mvt in mouvements if (maintenant - mvt['date_entree']) > vingt_minutes]
    ma = len(mouvements_filtrés)
    mouvements_filtrés=list(mouvements_filtrés)
    for doc in  mouvements_filtrés:
      camion = Camion.objects.get(id_cam=doc['camion_id'])
      doc['camion'] = camion
      ptr_etr = Utilisateurs.objects.get(id_user=doc['pointeur_entree_id'])
      doc['pointeur ']= ptr_etr
    return JsonResponse(list(mouvements_filtrés), safe=False)
    #return render(request, "pages/detail_urgent.html", {'mvt' :mouvements_filtrés ,'lg' :lg})

    #return mouvements_filtrés

def detail_urgent(request,id):
  vingt_minutes = timedelta(minutes=20)
  trt_minutes = timedelta(minutes=30)
  maintenant = timezone.now()
  mouvements = Mouvement1.objects.filter(date_sortie__isnull=True)
  mouvements_filtrés = [mvt for mvt in mouvements if (maintenant - mvt.date_entree) >= vingt_minutes and (maintenant - mvt.date_entree) < trt_minutes ]
  for mvt in mouvements_filtrés :
      poineur= Utilisateurs.objects.get(id_user=mvt.pointeur_entree_id)
      mvt.pointeur=poineur.fullname
      camion=Camion.objects.get(id_cam=mvt.camion_id)
      mvt.trans=camion.transporteur
      mvt.imat=camion.immatriculation
  lg=len(mouvements_filtrés)
  total_encours=len(mouvements)
  if total_encours >= 1 :
    pourcentage_urgent=(lg/total_encours) * 100
  else :
    pourcentage_urgent=0

  user = Utilisateurs.objects.get(id_user=id)
  context = {
    'segment': 'index',
    'mvt' : mouvements_filtrés,
    # 'products' : Product.objects.all()
      'lg' :lg,
      'pourcentage_urgent' :int(pourcentage_urgent),
      'util': user
  }

  return render(request, "pages/detail_urgent.html", context)

def detail_depassemnt(request, id):
    vingt_minutes = timedelta(minutes=31)
    maintenant = timezone.now()
    mouvements = Mouvement1.objects.filter(date_sortie__isnull=True)
    mouvements_filtrés = [mvt for mvt in mouvements if (maintenant - mvt.date_entree) > vingt_minutes]
    for mvt in mouvements_filtrés:
        poineur = Utilisateurs.objects.get(id_user=mvt.pointeur_entree_id)
        mvt.pointeur = poineur.fullname
        camion = Camion.objects.get(id_cam=mvt.camion_id)
        mvt.trans = camion.transporteur
        mvt.imat = camion.immatriculation
    lg = len(mouvements_filtrés)
    total_depassemnt=len(mouvements)
    if total_depassemnt >= 1:
       pourcentage_depassement = (lg / total_depassemnt) * 100
    else :
      pourcentage_depassement= 0
    user = Utilisateurs.objects.get(id_user=id)
    context = {
        'segment': 'index',
        'mvt': mouvements_filtrés,
        # 'products' : Product.objects.all()
        'lg': lg,
        'pourcentage_depassement' : int(pourcentage_depassement),
        'util': user
    }

    return render(request, "pages/detail_depassement.html", context)

def detail_plus_30(request, id):
    vingt_minutes = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements = Mouvement1.objects.filter(date_sortie__isnull=False)
    mouvements_filtrés = [mvt for mvt in mouvements if (mvt.date_sortie - mvt.date_entree) > vingt_minutes]
    for mvt in mouvements_filtrés:
        poineur = Utilisateurs.objects.get(id_user=mvt.pointeur_entree_id)
        mvt.pointeur = poineur.fullname

        poineur_srt = Utilisateurs.objects.get(id_user=mvt.pointeur_sortie_id)

        mvt.pointeur_srt = poineur_srt.fullname
        camion = Camion.objects.get(id_cam=mvt.camion_id)
        mvt.trans = camion.transporteur
        mvt.imat = camion.immatriculation
    lg = len(mouvements_filtrés)
    lg = len(mouvements_filtrés)
    total_plus_30 = len(mouvements)
    if total_plus_30 >= 1:
      pourcentage_plus_30 = (lg / total_plus_30) * 100
    else :
      pourcentage_plus_30=0
    user = Utilisateurs.objects.get(id_user=id)

    context = {
        'segment': 'index',
        'mvt': mouvements_filtrés,
        # 'products' : Product.objects.all()
        'lg': lg,
        'util': user,
        'pourcentage_plus_30' : int( pourcentage_plus_30)
    }

    return render(request, "pages/detail_plus_30.html", context)
def detail_moins_30(request, id):
    vingt_minutes = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements = Mouvement1.objects.filter(date_sortie__isnull=False)
    mouvements_filtrés = [mvt for mvt in mouvements if (mvt.date_sortie - mvt.date_entree) <= vingt_minutes]
    for mvt in mouvements_filtrés:
        poineur = Utilisateurs.objects.get(id_user=mvt.pointeur_entree_id)
        mvt.pointeur = poineur.fullname
        poineur_srt = Utilisateurs.objects.get(id_user=mvt.pointeur_sortie_id)
        mvt.pointeur_srt = poineur_srt.fullname
        camion = Camion.objects.get(id_cam=mvt.camion_id)
        mvt.trans = camion.transporteur
        mvt.imat = camion.immatriculation
    lg = len(mouvements_filtrés)
    total_moins_30 = len(mouvements)
    if  total_moins_30 >= 1 :
       pourcentage_moins_30 = (lg / total_moins_30) * 100
    else :
        pourcentage_moins_30=0
    user = Utilisateurs.objects.get(id_user=id)

    context = {
        'segment': 'index',
        'mvt': mouvements_filtrés,
        # 'products' : Product.objects.all()
        'lg': lg,
        'pourcentage_moins_30' :int(pourcentage_moins_30),
        'util': user
    }

    #return render(request, "pages/detail_depassement.html", context)
    return render(request, "pages/detail_moins_30.html", context)

@csrf_exempt
###Gesrion Connexion
def seconnecter(request):
    forms = LoginForm()
    #return render(request, 'pages/index.html')
    if request.method == 'POST':

      if 1:
        username = request.POST['email']
        password = request.POST['password']
        user = False
        try:
          user = Utilisateurs.objects.get(email=username, password=password)
          if user.poste == 'E1':
            camions = Camion.objects.all()
            return render(request, 'pages/index1.html', {'util': user,'camions': camions})
          elif user.poste == 'S1':
            return render(request, 'pages/index2.html', {'util': user})
          elif user.poste == 'SA':
            #return render(request, 'pages/gestion_utilisateurs.html', {'util': user})
            return  redirect("/liste_user/"+ str(user.id_user))
          elif user.poste == 'A1':
              return  redirect("/index/" + str(user.id_user))
          elif user.poste == 'E0':
              #return render(request, 'pages/mouvement_entre_0.html', {'util': user})
              return redirect("/entreedecalog_view/" + str(user.id_user))
          elif user.poste == 'A0':
              #return render(request, 'pages/mouvement_entre_0.html', {'util': user})
              return redirect("/index_dk_log/" + str(user.id_user))
          if user.poste == 'E2':
              camions = Camion.objects.all()
              return redirect("/index2_view/" + str(user.id_user))
          if user.poste == 'S2':
              camions = Camion.objects.all()
              return redirect("/index3_view/" + str(user.id_user))
          elif user.poste == 'S0':

             return redirect("/sortie_decalog_view/" + str(user.id_user))
          elif user.poste == 'A2':

             return redirect("/index_sacherie/" + str(user.id_user))

          else:
            #return (redirect('login'))

            return render(request, 'pages/login2.html')
            pass
        except:
          pass
          #return render(request, 'pages/se_conecter.html')
        #return render(request, 'pages/index.html', {'util': user})
        return render(request, 'pages/login2.html')


#################### La vue qui affiche la page login au démarrage de l'application #######################
def login_page(request):
  forms = LoginForm()
  if request.method == 'POST':
    forms = LoginForm(request.POST)
    if forms.is_valid() or 1:
      email = forms.cleaned_data['email']
      password = forms.cleaned_data['password']
      user = authenticate(email=email, password=password)
      if user:
        login(request, user)
        return redirect('dashboard')
  context = {'form': forms}
  return render(request, 'pages/login2.html', context)

######Gestio Post Entree
def liste_mouvements(request, id_user):
    mouvements = Mouvement1.objects.filter(date_entree__isnull=True).values('id_mvt', 'mission', 'camion_id',
                                                                            'statut_entree', 'statut_sortie',
                                                                            'chauffeur_id'
                                                                            , 'remorque')
    mouvement_list = list(mouvements)
    for mouvement in mouvement_list:
        camion_id = mouvement['camion_id']
        camion = Camion.objects.filter(id_cam=camion_id).values('id_cam', 'immatriculation', 'transporteur',
                                                                'type').first()
        mouvement['camion'] = camion
        chauffeur_id = mouvement['chauffeur_id']
        chauffeur = Chaffeur.objects.filter(id_chauffeur=chauffeur_id).values('id_chauffeur', 'fullname',
                                                                              'permis').first()
        mouvement['chauffeur'] = chauffeur
    response_data = {
        'mouvements': mouvement_list,
        'id_usr': id_user,  # Inclure l'ID de l'utilisateur dans la réponse JSON
    }
    return JsonResponse(response_data)


def index1_view(request, id_user):
  util = Utilisateurs.objects.get(id_user=id_user)
  camions = Camion.objects.all()
  return render(request, 'pages/index1.html', {'util': util, 'camions': camions})
def index2_view(request, id_user):
  util = Utilisateurs.objects.get(id_user=id_user)
  return render(request, 'pages/index2.html', {'util': util})
def entredecalon_view(request, id_user):
  util = Utilisateurs.objects.get(id_user=id_user)
  camions = Camion.objects.all()
  chauffeurs = Chaffeur.objects.all()
  return render(request, 'pages/mouvement_entre_0.html', {'util': util, 'camions': camions, 'chauffeurs': chauffeurs})
@csrf_exempt
def ajoutmouvement(request, id_user):
  try:
    util = Utilisateurs.objects.get(id_user=id_user)
  except Utilisateurs.DoesNotExist:
    return HttpResponse("L'utilisateur spécifié n'existe pas.", status=404)
  if request.method == 'POST':
    form = MouvementForm(request.POST)
    if form.is_valid():
      mouvement = form.save(commit=False)
      mouvement.date_entree = timezone.now()
      mouvement.camion_id = request.POST.get('camion')
      mouvement.statut_entree = request.POST.get('statut_entree')
      mouvement.remorque = request.POST.get('remorque')
      mouvement.permis = request.POST.get('permis')
      mouvement.mission = request.POST.get('mission')
      mouvement.pointeur_entree_id = util.id_user
      mouvement.save()
      camions = Camion.objects.all()
      return redirect(f'/index1_view/{util.id_user}')
  else:
    form = MouvementForm()
  camions = Camion.objects.all()
  return render(request, 'pages/ajouter_mouvement.html', {'form': form, 'camions': camions, 'util': util})

#####Gestion Sortie
def liste_mouvements1(request, id_user):
    mouvements = Mouvement1.objects.filter(date_entree__isnull=False,date_sortie__isnull=True).values('id_mvt','mission', 'camion_id', 'statut_entree', 'statut_sortie', 'chauffeur_id'
                                            , 'remorque')
    mouvement_list = list(mouvements)
    for mouvement in mouvement_list:
      camion_id = mouvement['camion_id']
      camion = Camion.objects.filter(id_cam=camion_id).values('id_cam', 'immatriculation', 'transporteur','type').first()
      mouvement['camion'] = camion
      chauffeur_id = mouvement['chauffeur_id']
      chauffeur = Chaffeur.objects.filter(id_chauffeur=chauffeur_id).values('id_chauffeur', 'fullname',
                                                                            'permis').first()
      mouvement['chauffeur'] = chauffeur
    response_data = {
      'mouvements': mouvement_list,
      'id_usr': id_user,  # Inclure l'ID de l'utilisateur dans la réponse JSON
    }
    return JsonResponse(response_data)
def liste_mouvementsdk1(request, id_user):
    mouvements = Mouvement0.objects.filter(date_entree__isnull=False,date_sortie__isnull=True).values('id_mvt', 'camion_id', 'statut_entree', 'statut_sortie', 'chauffeur_id'
                                            , 'remorque')
    mouvement_list = list(mouvements)
    for mouvement in mouvement_list:
      camion_id = mouvement['camion_id']
      camion = Camion.objects.filter(id_cam=camion_id).values('id_cam', 'immatriculation', 'transporteur','type').first()
      mouvement['camion'] = camion
      chauffeur_id = mouvement['chauffeur_id']
      chauffeur = Chaffeur.objects.filter(id_chauffeur=chauffeur_id).values('id_chauffeur', 'fullname',
                                                                            'permis').first()
      mouvement['chauffeur'] = chauffeur
    response_data = {
      'mouvements': mouvement_list,
      'id_usr': id_user,  # Inclure l'ID de l'utilisateur dans la réponse JSON
    }
    return JsonResponse(response_data)


def ajoutsortie(request):
    if request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            id_mvt = request.POST.get('id_mvt')
            id_user = request.POST.get('id_user')

            # Récupérer les objets Utilisateurs et Mouvement en fonction des IDs fournis
            util = get_object_or_404(Utilisateurs, id_user=id_user)
            mouvement = get_object_or_404(Mouvement1, id_mvt=id_mvt)

            # Mettre à jour les informations du mouvement
            mouvement.date_sortie = timezone.now()
            mouvement.pointeur_sortie_id = util.id_user
            mouvement.statut_sortie = form.cleaned_data.get(
                'statut_sortie')  # Récupérer le statut depuis les données validées du formulaire
            mouvement.save()

            # Rediriger vers une vue après sauvegarde
            #return redirect(f'/index2_view/{util.id_user}')
            return render(request, 'pages/index2.html', {'util': util})

    else:
        form = SortieForm()

    # Assurez-vous que 'mouvement' et 'util' sont définis si vous les utilisez dans le template
    return render(request, 'pages/ajoutsortiedp.html', {'form': form})

def ajoutsortiedk(request):
    if request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            id_mvt = request.POST.get('id_mvt')
            id_user = request.POST.get('id_user')

            # Récupérer les objets Utilisateurs et Mouvement en fonction des IDs fournis
            util = get_object_or_404(Utilisateurs, id_user=id_user)
            mouvement = get_object_or_404(Mouvement0, id_mvt=id_mvt)

            # Mettre à jour les informations du mouvement
            mouvement.date_sortie = timezone.now()
            mouvement.pointeur_sortie_id = util.id_user
            mouvement.statut_sortie = form.cleaned_data.get(
                'statut_sortie')  # Récupérer le statut depuis les données validées du formulaire
            mouvement.save()

            # Rediriger vers une vue après sauvegarde
            return redirect(f'/sortie_decalog_view/{util.id_user}')
    else:
        form = SortieForm()

    # Assurez-vous que 'mouvement' et 'util' sont définis si vous les utilisez dans le template
    return render(request, 'pages/ajoutsortiedp.html', {'form': form})
def tout_mouvement(request, id_mvt):
    user=Utilisateurs.objects.get(id_user=id_mvt)
    return render(request, 'pages/liste_mouvement.html', {'util': user})
def tout_mouvement0(request, id_mvt):
    user=Utilisateurs.objects.get(id_user=id_mvt)
    return render(request, 'pages/liste_mouvements0.html', {'util': user})
def tout_mouvement2(request, id_mvt):
    user=Utilisateurs.objects.get(id_user=id_mvt)
    return render(request, 'pages/liste_mouvement2.html', {'util': user})


def liste_mouvements2(request):
    mouvements = Mouvement1.objects.all().values('id_mvt','mission','camion_id', 'statut_entree', 'statut_sortie','chauffeur_id', 'remorque','date_entree','date_sortie','pointeur_sortie_id','pointeur_entree_id')
    mouvement_list = list(mouvements)
    for mouvement in mouvement_list:
        camion_id = mouvement['camion_id']
        camion = Camion.objects.filter(id_cam=camion_id).values('id_cam', 'immatriculation', 'transporteur').first()
        mouvement['camion'] = camion
        user_entre=Utilisateurs.objects.filter(id_user=mouvement['pointeur_entree_id']).values('fullname').first()
        if mouvement['pointeur_sortie_id']  :
            user_sortie= Utilisateurs.objects.filter(id_user=mouvement['pointeur_sortie_id']).values('fullname').first()
        else:
            user_sortie = Utilisateurs.objects.filter(id_user=1).values('fullname').first()
            #for user_sortie in user_sortie :
                # Mettre l'attribut fullname vide
            user_sortie = {'fullname': 'original_name'}
            user_sortie['fullname'] = 'null'

            #user_sortie='oo'

        mouvement['user_ert'] = user_entre
        mouvement['user_srt'] = user_sortie
        chauffeur_id = mouvement['chauffeur_id']
        chauffeur = Chaffeur.objects.filter(id_chauffeur=chauffeur_id).values('id_chauffeur', 'fullname',
                                                                              'permis').first()
        mouvement['chauffeur'] = chauffeur
    return JsonResponse(list(mouvement_list), safe=False)


def liste_mouvements_dk(request):
    mouvements = Mouvement0.objects.all().values('id_mvt','destination','camion_id', 'statut_entree', 'statut_sortie','chauffeur_id', 'remorque','date_entree','date_sortie','pointeur_sortie_id','pointeur_entree_id')
    mouvement_list = list(mouvements)
    for mouvement in mouvement_list:
        camion_id = mouvement['camion_id']
        camion = Camion.objects.filter(id_cam=camion_id).values('id_cam', 'immatriculation', 'transporteur').first()
        mouvement['camion'] = camion
        user_entre=Utilisateurs.objects.filter(id_user=mouvement['pointeur_entree_id']).values('fullname').first()
        if mouvement['pointeur_sortie_id']  :
            user_sortie= Utilisateurs.objects.filter(id_user=mouvement['pointeur_sortie_id']).values('fullname').first()
        else:
            user_sortie = Utilisateurs.objects.filter(id_user=1).values('fullname').first()
            #for user_sortie in user_sortie :
                # Mettre l'attribut fullname vide
            user_sortie = {'fullname': 'original_name'}
            user_sortie['fullname'] = 'null'

            #user_sortie='oo'

        mouvement['user_ert'] = user_entre
        mouvement['user_srt'] = user_sortie
        chauffeur_id = mouvement['chauffeur_id']
        chauffeur = Chaffeur.objects.filter(id_chauffeur=chauffeur_id).values('id_chauffeur', 'fullname',
                                                                              'permis').first()
        mouvement['chauffeur'] = chauffeur
    return JsonResponse(list(mouvement_list), safe=False)

def liste_mouvements_sacherie(request):
    mouvements = Mouvement2.objects.all().values('id_mvt','mission','camion_id', 'statut_entree', 'statut_sortie','chauffeur_id', 'remorque','date_entree','date_sortie','pointeur_sortie_id','pointeur_entree_id')
    mouvement_list = list(mouvements)
    for mouvement in mouvement_list:
        camion_id = mouvement['camion_id']
        camion = Camion.objects.filter(id_cam=camion_id).values('id_cam', 'immatriculation', 'transporteur').first()
        mouvement['camion'] = camion
        user_entre=Utilisateurs.objects.filter(id_user=mouvement['pointeur_entree_id']).values('fullname').first()
        if mouvement['pointeur_sortie_id']  :
            user_sortie= Utilisateurs.objects.filter(id_user=mouvement['pointeur_sortie_id']).values('fullname').first()
        else:
            user_sortie = Utilisateurs.objects.filter(id_user=1).values('fullname').first()
            #for user_sortie in user_sortie :
                # Mettre l'attribut fullname vide
            user_sortie = {'fullname': 'original_name'}
            user_sortie['fullname'] = 'null'

            #user_sortie='oo'

        mouvement['user_ert'] = user_entre
        mouvement['user_srt'] = user_sortie
        chauffeur_id = mouvement['chauffeur_id']
        chauffeur = Chaffeur.objects.filter(id_chauffeur=chauffeur_id).values('id_chauffeur', 'fullname',
                                                                              'permis').first()
        mouvement['chauffeur'] = chauffeur
    return JsonResponse(list(mouvement_list), safe=False)


@csrf_exempt
def modifier_mouvement(request):
    if request.method == 'POST':
      boite_id = request.POST['mouvementId']
      boite = get_object_or_404(Mouvement1, id_mvt=boite_id)
      id_cam=boite.camion_id
      id_chauff=boite.chauffeur_id
      boite.mission = request.POST['mission']
      boite.remorque = request.POST['remorque']
      boite.statut_entree = request.POST['statut_entree']
      boite.statut_sortie = request.POST['statut_sortie']

      if  request.POST['camion'] :
          try :
              cam_mof=Camion.objects.filter(immatriculation= request.POST['camion']).first()
              boite.camion_id=cam_mof.id_cam
          except :
           pass
      if  request.POST['permis'] :
          try :
              chau_mof=Chaffeur.objects.filter(permis= request.POST['permis']).first()
              boite.chauffeur_id=chau_mof.id_chauffeur
          except :
           pass



      boite.save()
      #return redirect(reverse('index'))  # Redirigez vers la page index après la modification
      return redirect("/liste_umvt/" + str(request.POST['id_user']))

    return render(request, 'index.html')

@csrf_exempt
def modifier_mouvement0(request):
    if request.method == 'POST':
      boite_id = request.POST['mouvementId']
      boite = get_object_or_404(Mouvement0, id_mvt=boite_id)
      boite.destination = request.POST['destination']
      boite.remorque = request.POST['remorque']
      boite.statut_entree = request.POST['statut_entree']
      boite.statut_sortie = request.POST['statut_sortie']

      if  request.POST['camion'] :
          try :
              cam_mof=Camion.objects.filter(immatriculation= request.POST['camion']).first()
              boite.camion_id=cam_mof.id_cam
          except :
           pass
      if  request.POST['permis'] :
          try :
              chau_mof=Chaffeur.objects.filter(permis= request.POST['permis']).first()
              boite.chauffeur_id=chau_mof.id_chauffeur
          except :
           pass



      boite.save()
      #return redirect(reverse('index'))  # Redirigez vers la page index après la modification
      return redirect("/liste_tt_mvt0/" + str(request.POST['id_user']))

    return render(request, 'index.html')

@csrf_exempt
def modifier_mouvement2(request):
    if request.method == 'POST':
      boite_id = request.POST['mouvementId']

      boite = get_object_or_404(Mouvement2, id_mvt=boite_id)
      status_sortie = boite.statut_sortie
      status_entree = boite.statut_entree
      #boite.immatriculation = request.POST['camion']
      #boite.transporteur = request.POST['trans']
      boite.mission = request.POST['mission']
      #boite.permis = request.POST['permis']
      boite.remorque = request.POST['remorque']
      boite.statut_entree= request.POST['statut_entree']
      boite.statut_sortie= request.POST['statut_sortie']

      if  request.POST['camion'] :
          try :
              cam_mof=Camion.objects.filter(immatriculation= request.POST['camion']).first()
              boite.camion_id=cam_mof.id_cam
          except :
           pass
      if  request.POST['permis'] :
          try :
              chau_mof=Chaffeur.objects.filter(permis= request.POST['permis']).first()
              boite.chauffeur_id=chau_mof.id_chauffeur
          except :
           pass



      boite.save()
      #return redirect(reverse('index'))  # Redirigez vers la page index après la modification
      return redirect("/liste_tt_mvt2/" + str(request.POST['id_user']))

    return render(request, 'index.html')


def activer_desactiver_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        status = request.POST.get('status')

        user = Utilisateurs.objects.get(id_user=user_id)  # Remplacez User par votre modèle utilisateur
        user.status = status
        user.save()

        return redirect(
        "/liste_user/" + str(request.POST.get('userid')))  # Remplacez 'your_view_name' par le nom de la vue que vous souhaitez rediriger après la mise à jour

def fetch_dshbord(request) :
        vingt_minutes = timedelta(minutes=20)
        trt_minutes = timedelta(minutes=30)
        maintenant = timezone.now()
        mouvements = Mouvement1.objects.filter(date_sortie__isnull=True)
        mouvements_filtrés = [mvt for mvt in mouvements if (maintenant - mvt.date_entree) >= vingt_minutes and (
                maintenant - mvt.date_entree) < trt_minutes]
        urg = len(mouvements_filtrés)
        ###Depassement

        mouvements_dep = Mouvement1.objects.filter(date_sortie__isnull=True)
        mouvements_filtrés_dep = [mvt for mvt in mouvements_dep if (maintenant - mvt.date_entree) >= trt_minutes]
        dep = len(mouvements_filtrés_dep)

        ###Plus 30
        vingt_minutes_30 = timedelta(minutes=30)
        maintenant = timezone.now()
        mouvements_30 = Mouvement1.objects.filter(date_sortie__isnull=False)
        mouvements_filtrés_30 = [mvt for mvt in mouvements_30 if (mvt.date_sortie - mvt.date_entree) >= trt_minutes]
        lg_30 = len(mouvements_filtrés_30)
        #####OIMS 30

        vingt_minutes_moin = timedelta(minutes=30)
        maintenant = timezone.now()
        mouvements_moins = Mouvement1.objects.filter(date_sortie__isnull=False)
        mouvements_filtrés_moins = [mvt for mvt in mouvements_moins if
                                    (mvt.date_sortie - mvt.date_entree) < trt_minutes]
        lg_moins = len(mouvements_filtrés_moins)
        mvt_total = Mouvement1.objects.filter(date_sortie__isnull=True)
        total_cours = len(mvt_total)
        totalter = lg_30 + lg_moins
        tout_mouvements = Mouvement1.objects.filter(date_sortie__isnull=True)[:50]
        vingt_minutes = timedelta(minutes=30)
        trt = timedelta(minutes=20)
        data=[]
        for mvt in tout_mouvements:
            diff = (maintenant - mvt.date_entree).total_seconds() / 60
            mvt.chrono = int(diff)

            # duree=math.ceil((mvt.date_sortie - mvt.date_entree).total_seconds() / 3600)
            duree = float(diff)
            if duree >= 30:
                mvt.etat = 3
            if duree < 30 and duree > 20:
                mvt.etat = 2
            if duree <= 20:
                mvt.etat = 1

            camion = Camion.objects.get(id_cam=mvt.camion_id)
            mvt.cam = camion.immatriculation
            user = Utilisateurs.objects.get(id_user=request.POST['id'])
            data.append({
                'dep' : dep ,
                'urg' : urg ,
            'moins' : lg_moins,
            'plus' : lg_30,
            'total_crs' :total_cours ,
            'total_ter' : totalter ,
            'etat' : mvt.etat,
                'date_entree' :mvt.date_entree,
                'chrono' : mvt.chrono,
                'mission' :mvt.mission,
                'cam' : mvt.cam



            })

        return JsonResponse({'data': data})


##################3Gestion

def liste_mouvements_0(request):
    mouvements = Mouvement0.objects.all().values('id_mvt','camion_id', 'statut_entree', 'statut_sortie','chauffeur_id', 'remorque','date_entree','date_sortie','pointeur_sortie_id','pointeur_entree_id','destination')
    mouvement_list = list(mouvements)
    for mouvement in mouvement_list:
        camion_id = mouvement['camion_id']
        camion = Camion.objects.filter(id_cam=camion_id).values('id_cam', 'immatriculation', 'transporteur','type').first()
        mouvement['camion'] = camion
        user_entre=Utilisateurs.objects.filter(id_user=mouvement['pointeur_entree_id']).values('fullname').first()
        if mouvement['pointeur_sortie_id']  :
            user_sortie= Utilisateurs.objects.filter(id_user=mouvement['pointeur_sortie_id']).values('fullname').first()
        else:
            user_sortie = Utilisateurs.objects.filter(id_user=1).values('fullname').first()
            #for user_sortie in user_sortie :
                # Mettre l'attribut fullname vide
            user_sortie = {'fullname': 'original_name'}
            user_sortie['fullname'] = 'null'

            #user_sortie='oo'

        mouvement['user_ert'] = user_entre
        mouvement['user_srt'] = user_sortie
        chauffeur_id = mouvement['chauffeur_id']
        chauffeur = Chaffeur.objects.filter(id_chauffeur=chauffeur_id).values('id_chauffeur', 'fullname',
                                                                              'permis').first()
        mouvement['chauffeur'] = chauffeur
    return JsonResponse(list(mouvement_list), safe=False)
def ajouter_mouvements_0(request):
    ###ajout mvt 0
    ####copie mvt 1
    return  redirect("/entreedecalog_view/" + str(request.POST['id_user']))


def ajoutmouvement0(request, id_user):
    try:
        util = Utilisateurs.objects.get(id_user=id_user)
    except Utilisateurs.DoesNotExist:
        return HttpResponse("L'utilisateur spécifié n'existe pas.", status=404)
    if request.method == 'POST':
            mouvement0 = Mouvement0()
            mouvement0.date_entree = timezone.now()
            mouvement0.camion_id = request.POST.get('camion')
            mouvement0.chauffeur_id = request.POST.get('chauffeur')
            mouvement0.statut_entree = request.POST.get('statut_entree')
            mouvement0.destination = request.POST.get('destination')
            remorque=''
            camion = Camion.objects.get(id_cam=mouvement0.camion_id)
            if (camion.type != 'SEMI-REMORQUE'):
                    remorque = camion.immatriculation
            else:
                    remorque = request.POST.get('remorque')
            mouvement0.remorque = remorque
            mouvement0.pointeur_entree_id = util.id_user
            mouvement0.save()
            mvt0=Mouvement0.objects.filter(Q(destination__endswith='tom') | Q(destination__endswith='sacherie')).last()
            if  mouvement0.destination.endswith('tom') :
                mouvement1 = Mouvement1()
                mouvement1.camion_id = request.POST.get('camion')
                mouvement1.chauffeur_id = request.POST.get('chauffeur')
                mouvement1.statut_entree = request.POST.get('statut_entree')
                mouvement1.remorque=remorque
                mouvement1.id_mvt_0_id=mvt0.id_mvt
                mouvement1.pointeur_entree_id = util.id_user
                mouvement1.save()
            elif (mouvement0.destination.endswith('sacherie')):
                mouvement2 = Mouvement2()
                mouvement2.camion_id = request.POST.get('camion')
                mouvement2.chauffeur_id = request.POST.get('chauffeur')
                mouvement2.statut_entree = request.POST.get('statut_entree')
                mouvement2.remorque=remorque
                mouvement2.id_mvt_0_id=mvt0.id_mvt
                mouvement2.pointeur_entree_id = util.id_user
                mouvement2.save()

            #return render('pages/mouvement_entre_0.html', {'util': util})
            return  redirect("/entreedecalog_view/" + str(util.id_user))

    else:
        chauffeurs = Chaffeur.objects.all()
        camions = Camion.objects.all()
        return render(request, 'pages/mouvement_entre_0.html', {'camions': camions,'util': util, 'chauffeurs': chauffeurs,})
    chauffeurs = Chaffeur.objects.all()
    camions = Camion.objects.all()
    return render(request, 'pages/mouvement_entre_0.html', {'form': form, 'camions': camions,'util': util, 'chauffeurs': chauffeurs,})

def entree_tom(request):
    if request.method == 'POST':
        id_mvt = request.POST.get('id_mvt')
        id_user = request.POST.get('id_user')
        # Récupérer les objets Utilisateurs et Mouvement en fonction des IDs fournis
        util = get_object_or_404(Utilisateurs, id_user=id_user)
        mouvement = get_object_or_404(Mouvement1, id_mvt=id_mvt)
        mouvement.pointeur_entree_id = util.id_user
        mouvement.date_entree = timezone.now()
        mouvement.mission = request.POST.get('mission')
        mouvement.save()
        return redirect('/index1_view/' + str(util.id_user))



def entree_camion(request):
    if request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            id_mvt = request.POST.get('id_mvt')
            id_user = request.POST.get('id_user')

            # Récupérer les objets Utilisateurs et Mouvement en fonction des IDs fournis
            util = get_object_or_404(Utilisateurs, id_user=id_user)
            mouvement = get_object_or_404(Mouvement1, id_mvt=id_mvt)

            mouvement.date_entree = timezone.now()
            mouvement.mission =  request.POST.get(
                'mission')  # Récupérer le statut depuis les données validées du formulaire
            mouvement.save()

            # Rediriger vers une vue après sauvegarde
            return redirect(f'/index1_view/{util.id_user}')
    else:
        form = SortieForm()

    # Assurez-vous que 'mouvement' et 'util' sont définis si vous les utilisez dans le template
    return render(request, 'pages/ajoutsortiedp.html', {'form': form})

def sortie_decalog_view(request, id_user):
  util = Utilisateurs.objects.get(id_user=id_user)
  return render(request, 'pages/mouvement_sortie_0.html', {'util': util})


@csrf_exempt

def ajouter_camion_dk_log(request):
    if request.method == 'POST':
        form = CamionForm(request.POST)
        if form.is_valid() or 1:
            camion = form.save()
            # Retourner une réponse JSON indiquant le succès de l'enregistrement
            return JsonResponse({'success': True})
        else:
            # Retourner une réponse JSON avec des erreurs de formulaire
            return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'errors': 'Méthode non autorisée'})

@csrf_exempt

def ajouter_chauffeur(request):
    if request.method == 'POST':
        form = ChauffeurForm(request.POST)
        if form.is_valid():
            chauffeur = form.save()
            # Retourner une réponse JSON indiquant le succès de l'enregistrement
            #return JsonResponse({'success': True, 'chauffeur': {'id': chauffeur.id_chauffeur, 'fullname': chauffeur.fullname}})
            return JsonResponse(
                {'success': True})
        else:
            # Retourner une réponse JSON avec des erreurs de formulaire
            return JsonResponse({'success': False, 'errors': form.errors})

    return JsonResponse({'success': False, 'errors': 'Méthode non autorisée'})


def fetch_camion(request):
    camions=Camion.objects.all().values('id_cam','transporteur','immatriculation','type')
    return JsonResponse(list(camions), safe=False)


def fetch_chauffeur(request):
    chauffeurs=Chaffeur.objects.all().values('id_chauffeur','fullname','permis')
    return JsonResponse(list(chauffeurs), safe=False)


def index_dk(request,id):
    vingt_minutes = timedelta(minutes=20)
    trt_minutes = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements = Mouvement0.objects.filter(date_sortie__isnull=True)
    mouvements_filtrés = [mvt for mvt in mouvements if (maintenant - mvt.date_entree) >= vingt_minutes and (
                maintenant - mvt.date_entree) < trt_minutes]
    urg = len(mouvements_filtrés)
   ###Depassement

    mouvements_dep = Mouvement0.objects.filter(date_sortie__isnull=True)
    mouvements_filtrés_dep = [mvt for mvt in mouvements_dep if (maintenant - mvt.date_entree) >= trt_minutes]
    dep = len(mouvements_filtrés_dep)

    ###Plus 30
    vingt_minutes_30 = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements_30 = Mouvement0.objects.filter(date_sortie__isnull=False)
    mouvements_filtrés_30 = [mvt for mvt in mouvements_30 if (mvt.date_sortie - mvt.date_entree) >= trt_minutes]
    lg_30 = len(mouvements_filtrés_30)
    #####OIMS 30

    vingt_minutes_moin = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements_moins = Mouvement0.objects.filter(date_sortie__isnull=False)
    mouvements_filtrés_moins = [mvt for mvt in mouvements_moins if
                                (mvt.date_sortie - mvt.date_entree) < trt_minutes]
    lg_moins = len(mouvements_filtrés_moins)
    mvt_total=Mouvement0.objects.filter(date_sortie__isnull=True)
    total_cours =len(mvt_total)
    totalter = lg_30 + lg_moins
    tout_mouvements= Mouvement0.objects.filter(date_sortie__isnull=True)[:5]
    vingt_minutes = timedelta(minutes=30)
    trt = timedelta(minutes=20)


    for mvt in tout_mouvements :
        diff = (maintenant - mvt.date_entree).total_seconds()/60
        mvt.chrono=int(diff)

        #duree=math.ceil((mvt.date_sortie - mvt.date_entree).total_seconds() / 3600)
        duree=float(diff)
        if duree >=30 :
            mvt.etat= 3
        if duree <30 and duree > 20 :
            mvt.etat= 2
        if duree <= 20 :
          mvt.etat= 1

        camion=Camion.objects.get(id_cam=mvt.camion_id)
        mvt.cam=camion.immatriculation
    user=Utilisateurs.objects.get(id_user=id)
    return render(request, 'pages/index_dk_log.html',
                  { 'urg': urg, 'dep': dep, 'lg_30': lg_30, 'lg_mois': lg_moins,
                   'total_cours': total_cours, 'total_ter': totalter,'mvt':tout_mouvements,'util' :user})


########################Gestion Sacherie

def index2_view(request, id):
  util = Utilisateurs.objects.get(id_user=id)
  camions = Camion.objects.all()
  return render(request, 'pages/entree_mouvement_1.html', {'util': util, 'camions': camions})
def index3_view(request, id):
  util = Utilisateurs.objects.get(id_user=id)
  camions = Camion.objects.all()
  return render(request, 'pages/sortie_mouvement_1.html', {'util': util, 'camions': camions})
def entree_sacherie(request):
    if request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            id_mvt = request.POST.get('id_mvt')
            id_user = request.POST.get('id_user')

            # Récupérer les objets Utilisateurs et Mouvement en fonction des IDs fournis
            util = get_object_or_404(Utilisateurs, id_user=id_user)
            mouvement = get_object_or_404(Mouvement2, id_mvt=id_mvt)

            mouvement.date_entree = timezone.now()
            mouvement.mission =  request.POST.get(
                'mission')  # Récupérer le statut depuis les données validées du formulaire
            mouvement.save()

            # Rediriger vers une vue après sauvegarde
            return redirect(f'/index2_view/{util.id_user}')
    else:
        form = SortieForm()

    # Assurez-vous que 'mouvement' et 'util' sont définis si vous les utilisez dans le template
    return render(request, 'pages/ajoutsortiedp.html', {'form': form})



def ajoutsortie_sacherie(request):

        if request.method == 'POST':
            form = SortieForm(request.POST)
            if form.is_valid():
                id_mvt = request.POST.get('id_mvt')
                id_user = request.POST.get('id_user')

                # Récupérer les objets Utilisateurs et Mouvement en fonction des IDs fournis
                util = get_object_or_404(Utilisateurs, id_user=id_user)
                mouvement = get_object_or_404(Mouvement2, id_mvt=id_mvt)

                # Mettre à jour les informations du mouvement
                mouvement.date_sortie = timezone.now()
                mouvement.pointeur_sortie_id = util.id_user
                mouvement.statut_sortie = form.cleaned_data.get(
                    'statut_sortie')  # Récupérer le statut depuis les données validées du formulaire
                mouvement.save()

                # Rediriger vers une vue après sauvegarde
                return redirect(f'/index3_view/{util.id_user}')

        else:
            form = SortieForm()

        # Assurez-vous que 'mouvement' et 'util' sont définis si vous les utilisez dans le template
        return render(request, 'pages/ajoutsortiedp.html', {'form': form})


def liste_mouvements_3(request, id_user):
    mouvements = Mouvement2.objects.filter(date_entree__isnull=True).values('id_mvt', 'mission', 'camion_id',
                                                                            'statut_entree', 'statut_sortie',
                                                                            'chauffeur_id'
                                                                            , 'remorque')
    mouvement_list = list(mouvements)
    for mouvement in mouvement_list:
        camion_id = mouvement['camion_id']
        camion = Camion.objects.filter(id_cam=camion_id).values('id_cam', 'immatriculation', 'transporteur',
                                                                'type').first()
        mouvement['camion'] = camion
        chauffeur_id = mouvement['chauffeur_id']
        chauffeur = Chaffeur.objects.filter(id_chauffeur=chauffeur_id).values('id_chauffeur', 'fullname',
                                                                              'permis').first()
        mouvement['chauffeur'] = chauffeur
    response_data = {
        'mouvements': mouvement_list,
        'id_usr': id_user,  # Inclure l'ID de l'utilisateur dans la réponse JSON
    }
    return JsonResponse(response_data)



def liste_mouvements4(request, id_user):
    mouvements = Mouvement2.objects.filter(date_entree__isnull=False,date_sortie__isnull=True).values('id_mvt','mission', 'camion_id', 'statut_entree', 'statut_sortie', 'chauffeur_id'
                                            , 'remorque')
    mouvement_list = list(mouvements)
    for mouvement in mouvement_list:
      camion_id = mouvement['camion_id']
      camion = Camion.objects.filter(id_cam=camion_id).values('id_cam', 'immatriculation', 'transporteur','type').first()
      mouvement['camion'] = camion
      chauffeur_id = mouvement['chauffeur_id']
      chauffeur = Chaffeur.objects.filter(id_chauffeur=chauffeur_id).values('id_chauffeur', 'fullname',
                                                                            'permis').first()
      mouvement['chauffeur'] = chauffeur
    response_data = {
      'mouvements': mouvement_list,
      'id_usr': id_user,  # Inclure l'ID de l'utilisateur dans la réponse JSON
    }
    return JsonResponse(response_data)


def fetch_camion(request):
    camions=Camion.objects.all().values('id_cam','transporteur','immatriculation','type')
    return JsonResponse(list(camions), safe=False)


def fetch_chauffeur(request):
    chauffeurs=Chaffeur.objects.all().values('id_chauffeur','fullname','permis')
    return JsonResponse(list(chauffeurs), safe=False)









def index_sacherie(request,id):
    vingt_minutes = timedelta(minutes=20)
    trt_minutes = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements = Mouvement2.objects.filter(date_entree__isnull=False,date_sortie__isnull=True)
    mouvements_filtrés = [mvt for mvt in mouvements if (maintenant - mvt.date_entree) >= vingt_minutes and (
                maintenant - mvt.date_entree) < trt_minutes]
    urg = len(mouvements_filtrés)
   ###Depassement

    mouvements_dep = Mouvement2.objects.filter(date_entree__isnull=False,date_sortie__isnull=True)
    mouvements_filtrés_dep = [mvt for mvt in mouvements_dep if (maintenant - mvt.date_entree) >= trt_minutes]
    dep = len(mouvements_filtrés_dep)

    ###Plus 30
    vingt_minutes_30 = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements_30 = Mouvement2.objects.filter(date_entree__isnull=False,date_sortie__isnull=False)
    mouvements_filtrés_30 = [mvt for mvt in mouvements_30 if (mvt.date_sortie - mvt.date_entree) >= trt_minutes]
    lg_30 = len(mouvements_filtrés_30)
    #####OIMS 30

    vingt_minutes_moin = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements_moins = Mouvement2.objects.filter(date_entree__isnull=False,date_sortie__isnull=False)
    mouvements_filtrés_moins = [mvt for mvt in mouvements_moins if
                                (mvt.date_sortie - mvt.date_entree) < trt_minutes]
    lg_moins = len(mouvements_filtrés_moins)
    mvt_total=Mouvement2.objects.filter(date_entree__isnull=False,date_sortie__isnull=True)
    total_cours =len(mvt_total)
    totalter = lg_30 + lg_moins
    tout_mouvements= Mouvement2.objects.filter(date_entree__isnull=False,date_sortie__isnull=True)[:5]
    vingt_minutes = timedelta(minutes=30)
    trt = timedelta(minutes=20)


    for mvt in tout_mouvements :
        diff = (maintenant - mvt.date_entree).total_seconds()/60
        mvt.chrono=int(diff)

        #duree=math.ceil((mvt.date_sortie - mvt.date_entree).total_seconds() / 3600)
        duree=float(diff)
        if duree >=30 :
            mvt.etat= 3
        if duree <30 and duree > 20 :
            mvt.etat= 2
        if duree <= 20 :
          mvt.etat= 1

        camion=Camion.objects.get(id_cam=mvt.camion_id)
        mvt.cam=camion.immatriculation
    user=Utilisateurs.objects.get(id_user=id)
    return render(request, 'pages/index_sacherie.html',
                  { 'urg': urg, 'dep': dep, 'lg_30': lg_30, 'lg_mois': lg_moins,
                   'total_cours': total_cours, 'total_ter': totalter,'mvt':tout_mouvements,'util' :user})




###############Gestion details Sacherie

############Gestion Detail



def detail_urgent_sacherie(request,id):
  vingt_minutes = timedelta(minutes=20)
  trt_minutes = timedelta(minutes=30)
  maintenant = timezone.now()
  mouvements = Mouvement2.objects.filter(date_entree__isnull=False,date_sortie__isnull=True)
  mouvements_filtrés = [mvt for mvt in mouvements if (maintenant - mvt.date_entree) >= vingt_minutes and (maintenant - mvt.date_entree) < trt_minutes ]
  for mvt in mouvements_filtrés :
      poineur= Utilisateurs.objects.get(id_user=mvt.pointeur_entree_id)
      mvt.pointeur=poineur.fullname
      camion=Camion.objects.get(id_cam=mvt.camion_id)
      mvt.trans=camion.transporteur
      mvt.imat=camion.immatriculation
  lg=len(mouvements_filtrés)
  total_encours=len(mouvements)
  if total_encours >= 1 :
    pourcentage_urgent=(lg/total_encours) * 100
  else :
    pourcentage_urgent=0

  user = Utilisateurs.objects.get(id_user=id)
  context = {
    'segment': 'index',
    'mvt' : mouvements_filtrés,
    # 'products' : Product.objects.all()
      'lg' :lg,
      'pourcentage_urgent' :int(pourcentage_urgent),
      'util': user
  }

  return render(request, "pages/detail_urgent_sacherie.html", context)

def detail_depassement_sacherie(request, id):
    vingt_minutes = timedelta(minutes=31)
    maintenant = timezone.now()
    mouvements = Mouvement2.objects.filter(date_entree__isnull=False,date_sortie__isnull=True)
    mouvements_filtrés = [mvt for mvt in mouvements if (maintenant - mvt.date_entree) > vingt_minutes]
    for mvt in mouvements_filtrés:
        poineur = Utilisateurs.objects.get(id_user=mvt.pointeur_entree_id)
        mvt.pointeur = poineur.fullname
        camion = Camion.objects.get(id_cam=mvt.camion_id)
        mvt.trans = camion.transporteur
        mvt.imat = camion.immatriculation
    lg = len(mouvements_filtrés)
    total_depassemnt=len(mouvements)
    if total_depassemnt >= 1:
       pourcentage_depassement = (lg / total_depassemnt) * 100
    else :
      pourcentage_depassement= 0
    user = Utilisateurs.objects.get(id_user=id)
    context = {
        'segment': 'index',
        'mvt': mouvements_filtrés,
        # 'products' : Product.objects.all()
        'lg': lg,
        'pourcentage_depassement' : int(pourcentage_depassement),
        'util': user
    }

    return render(request, "pages/detail_depassement_sacherie.html", context)

def detail_plus_30_sacherie(request, id):
    vingt_minutes = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements = Mouvement2.objects.filter(date_entree__isnull=False,date_sortie__isnull=False)
    mouvements_filtrés = [mvt for mvt in mouvements if (mvt.date_sortie - mvt.date_entree) > vingt_minutes]
    for mvt in mouvements_filtrés:
        poineur = Utilisateurs.objects.get(id_user=mvt.pointeur_entree_id)
        mvt.pointeur = poineur.fullname

        poineur_srt = Utilisateurs.objects.get(id_user=mvt.pointeur_sortie_id)

        mvt.pointeur_srt = poineur_srt.fullname
        camion = Camion.objects.get(id_cam=mvt.camion_id)
        mvt.trans = camion.transporteur
        mvt.imat = camion.immatriculation
    lg = len(mouvements_filtrés)
    lg = len(mouvements_filtrés)
    total_plus_30 = len(mouvements)
    if total_plus_30 >= 1:
      pourcentage_plus_30 = (lg / total_plus_30) * 100
    else :
      pourcentage_plus_30=0
    user = Utilisateurs.objects.get(id_user=id)

    context = {
        'segment': 'index',
        'mvt': mouvements_filtrés,
        # 'products' : Product.objects.all()
        'lg': lg,
        'util': user,
        'pourcentage_plus_30' : int( pourcentage_plus_30)
    }

    return render(request, "pages/detail_plus_30_sacherie.html", context)
def detail_moins_30_sacherie(request, id):
    vingt_minutes = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements = Mouvement2.objects.filter(date_entree__isnull=False,date_sortie__isnull=False)
    mouvements_filtrés = [mvt for mvt in mouvements if (mvt.date_sortie - mvt.date_entree) <= vingt_minutes]
    for mvt in mouvements_filtrés:
        poineur = Utilisateurs.objects.get(id_user=mvt.pointeur_entree_id)
        mvt.pointeur = poineur.fullname
        poineur_srt = Utilisateurs.objects.get(id_user=mvt.pointeur_sortie_id)
        mvt.pointeur_srt = poineur_srt.fullname
        camion = Camion.objects.get(id_cam=mvt.camion_id)
        mvt.trans = camion.transporteur
        mvt.imat = camion.immatriculation
    lg = len(mouvements_filtrés)
    total_moins_30 = len(mouvements)
    if  total_moins_30 >= 1 :
       pourcentage_moins_30 = (lg / total_moins_30) * 100
    else :
        pourcentage_moins_30=0
    user = Utilisateurs.objects.get(id_user=id)

    context = {
        'segment': 'index',
        'mvt': mouvements_filtrés,
        # 'products' : Product.objects.all()
        'lg': lg,
        'pourcentage_moins_30' :int(pourcentage_moins_30),
        'util': user
    }

    #return render(request, "pages/detail_depassement.html", context)
    return render(request, "pages/detail_moins_30_sacherie.html", context)

################Detail DK LOG
############Gestion Detail



def detail_urgent_dk_log(request,id):
  vingt_minutes = timedelta(minutes=20)
  trt_minutes = timedelta(minutes=30)
  maintenant = timezone.now()
  mouvements = Mouvement0.objects.filter(date_entree__isnull=False,date_sortie__isnull=True)
  mouvements_filtrés = [mvt for mvt in mouvements if (maintenant - mvt.date_entree) >= vingt_minutes and (maintenant - mvt.date_entree) < trt_minutes ]
  for mvt in mouvements_filtrés :
      poineur= Utilisateurs.objects.get(id_user=mvt.pointeur_entree_id)
      mvt.pointeur=poineur.fullname
      camion=Camion.objects.get(id_cam=mvt.camion_id)
      mvt.trans=camion.transporteur
      mvt.imat=camion.immatriculation
  lg=len(mouvements_filtrés)
  total_encours=len(mouvements)
  if total_encours >= 1 :
    pourcentage_urgent=(lg/total_encours) * 100
  else :
    pourcentage_urgent=0

  user = Utilisateurs.objects.get(id_user=id)
  context = {
    'segment': 'index',
    'mvt' : mouvements_filtrés,
    # 'products' : Product.objects.all()
      'lg' :lg,
      'pourcentage_urgent' :int(pourcentage_urgent),
      'util': user
  }

  return render(request, "pages/detail_urgent_dk_log.html", context)

def detail_depassement_dk_log(request, id):
    vingt_minutes = timedelta(minutes=31)
    maintenant = timezone.now()
    mouvements = Mouvement0.objects.filter(date_entree__isnull=False,date_sortie__isnull=True)
    mouvements_filtrés = [mvt for mvt in mouvements if (maintenant - mvt.date_entree) > vingt_minutes]
    for mvt in mouvements_filtrés:
        poineur = Utilisateurs.objects.get(id_user=mvt.pointeur_entree_id)
        mvt.pointeur = poineur.fullname
        camion = Camion.objects.get(id_cam=mvt.camion_id)
        mvt.trans = camion.transporteur
        mvt.imat = camion.immatriculation
    lg = len(mouvements_filtrés)
    total_depassemnt=len(mouvements)
    if total_depassemnt >= 1:
       pourcentage_depassement = (lg / total_depassemnt) * 100
    else :
      pourcentage_depassement= 0
    user = Utilisateurs.objects.get(id_user=id)
    context = {
        'segment': 'index',
        'mvt': mouvements_filtrés,
        # 'products' : Product.objects.all()
        'lg': lg,
        'pourcentage_depassement' : int(pourcentage_depassement),
        'util': user
    }

    return render(request, "pages/detail_depasseme_dk_log.html", context)

def detail_plus_30_dk_log(request, id):
    vingt_minutes = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements = Mouvement0.objects.filter(date_entree__isnull=False,date_sortie__isnull=False)
    mouvements_filtrés = [mvt for mvt in mouvements if (mvt.date_sortie - mvt.date_entree) > vingt_minutes]
    for mvt in mouvements_filtrés:
        poineur = Utilisateurs.objects.get(id_user=mvt.pointeur_entree_id)
        mvt.pointeur = poineur.fullname

        poineur_srt = Utilisateurs.objects.get(id_user=mvt.pointeur_sortie_id)

        mvt.pointeur_srt = poineur_srt.fullname
        camion = Camion.objects.get(id_cam=mvt.camion_id)
        mvt.trans = camion.transporteur
        mvt.imat = camion.immatriculation
    lg = len(mouvements_filtrés)
    lg = len(mouvements_filtrés)
    total_plus_30 = len(mouvements)
    if total_plus_30 >= 1:
      pourcentage_plus_30 = (lg / total_plus_30) * 100
    else :
      pourcentage_plus_30=0
    user = Utilisateurs.objects.get(id_user=id)

    context = {
        'segment': 'index',
        'mvt': mouvements_filtrés,
        # 'products' : Product.objects.all()
        'lg': lg,
        'util': user,
        'pourcentage_plus_30' : int( pourcentage_plus_30)
    }

    return render(request, "pages/detail_plus_30_dk_log.html", context)
def detail_moins_30_dk_log(request, id):
    vingt_minutes = timedelta(minutes=30)
    maintenant = timezone.now()
    mouvements = Mouvement0.objects.filter(date_entree__isnull=False,date_sortie__isnull=False)
    mouvements_filtrés = [mvt for mvt in mouvements if (mvt.date_sortie - mvt.date_entree) <= vingt_minutes]
    for mvt in mouvements_filtrés:
        poineur = Utilisateurs.objects.get(id_user=mvt.pointeur_entree_id)
        mvt.pointeur = poineur.fullname
        poineur_srt = Utilisateurs.objects.get(id_user=mvt.pointeur_sortie_id)
        mvt.pointeur_srt = poineur_srt.fullname
        camion = Camion.objects.get(id_cam=mvt.camion_id)
        mvt.trans = camion.transporteur
        mvt.imat = camion.immatriculation
    lg = len(mouvements_filtrés)
    total_moins_30 = len(mouvements)
    if  total_moins_30 >= 1 :
       pourcentage_moins_30 = (lg / total_moins_30) * 100
    else :
        pourcentage_moins_30=0
    user = Utilisateurs.objects.get(id_user=id)

    context = {
        'segment': 'index',
        'mvt': mouvements_filtrés,
        # 'products' : Product.objects.all()
        'lg': lg,
        'pourcentage_moins_30' :int(pourcentage_moins_30),
        'util': user
    }

    #return render(request, "pages/detail_depassement.html", context)
    return render(request, "pages/detail_moins_30_dk_log.html", context)

#####################Extraction

def export_camions(request):
  if request.method == 'POST':
    # Access camion data from your model (replace with your logic)
    camions = Camion.objects.all()

    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Camions"

    # Write table header
    ws.append(["IMMATRICULATION", "Transporteur", "Type"])

    # Write camion data to rows
    for camion in camions:
      ws.append([camion.immatriculation, camion.transporteur, camion.type])

    # Create a response object and set content type to Excel
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=camions.xlsx'

    # Write the workbook to the response
    wb.save(response)
    return response

  else:
    # Handle invalid request method (optional)
    return HttpResponseBadRequest()



def export_mouvement0(request):
    if request.method == 'POST':
        # Récupérer les données des mouvements
        mouvements = Mouvement0.objects.filter(
            date_entree__isnull=False,
            date_sortie__isnull=False
        ).values(
            'id_mvt', 'chauffeur_id', 'camion_id', 'statut_entree', 'statut_sortie',
            'remorque', 'date_entree', 'pointeur_entree_id', 'date_sortie', 'pointeur_sortie_id'
        )

        mouvement_list = list(mouvements)
        for mouvement in mouvement_list:
            ################# STATUT ENTREE TEXT ###########
            if mouvement['statut_entree']== 0:
                mouvement['statut_entree'] = 'NON CHARGE'
            elif mouvement['statut_entree'] == 1 :
                mouvement['statut_entree'] = 'NON CHARGE'
            else:
                mouvement['statut_entree'] = 'Vide'
                ################# STATUT SORTIE TEXT ###########
            if mouvement['statut_sortie'] == 0:
                 mouvement['statut_sortie'] = 'NON CHARGE'
            elif mouvement['statut_sortie'] == 1:
                 mouvement['statut_sortie'] = 'NON CHARGE'
            else:
                 mouvement['statut_sortie'] = 'Vide'
            ############## CAMION #####################
            camion_id = mouvement['camion_id']
            camion = Camion.objects.get(id_cam=camion_id)
            mouvement['transporteur'] = camion.transporteur
            mouvement['type'] = camion.type
            mouvement['immatriculation'] = camion.immatriculation
            ################### CHAUFFEUR ###################
            chauffeur_id = mouvement['chauffeur_id']
            chauffeur = Chaffeur.objects.get(id_chauffeur=chauffeur_id)
            mouvement['chauffeur_name'] = chauffeur.fullname
            mouvement['permis'] = chauffeur.permis
            ################## POINTEUR ENTREE ##############
            pointeur_entree_id = mouvement['pointeur_entree_id']
            Pointeur_entree = Utilisateurs.objects.get(id_user=pointeur_entree_id)
            mouvement['pointeur_entree_name'] = Pointeur_entree.fullname
            ################## POINTEUR SORTIE ##############
            pointeur_sortie_id = mouvement['pointeur_sortie_id']
            Pointeur_sortie = Utilisateurs.objects.get(id_user=pointeur_sortie_id)
            mouvement['pointeur_sortie_name'] = Pointeur_sortie.fullname
        # Créer un nouveau workbook Excel
        wb = Workbook()
        ws = wb.active
        ws.title = "Camions"
        ws.append([
            "Statut Entree", "Statut Sortie", "Camion", "Transporteur", "Type", "Remorque",
            "Chauffeur", "Permis", "Date Entrée", "Pointeur Entrée", "Date Sortie", "Pointeur Sortie"
        ])
        for mouvement in mouvement_list:
            ws.append([
                mouvement['statut_entree'], mouvement['statut_sortie'], mouvement['immatriculation'],
                mouvement['transporteur'], mouvement['type'], mouvement['remorque'],
                mouvement['chauffeur_name'], mouvement['permis'], str(mouvement['date_entree']),
                mouvement['pointeur_entree_name'], str(mouvement['date_sortie']), mouvement['pointeur_sortie_name']
            ])
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="mouvements.xlsx"'

        wb.save(response)
        return response

    else:
        return HttpResponseBadRequest()



def export_mouvement2(request):
    if request.method == 'POST':
        # Récupérer les données des mouvements
        mouvements = Mouvement2.objects.filter(
            date_entree__isnull=False,
            date_sortie__isnull=False
        ).values(
            'id_mvt', 'chauffeur_id', 'camion_id', 'statut_entree', 'statut_sortie',
            'remorque', 'date_entree', 'pointeur_entree_id', 'date_sortie', 'pointeur_sortie_id','mission'
        )

        mouvement_list = list(mouvements)
        for mouvement in mouvement_list:
            ################# STATUT ENTREE TEXT ###########
            if mouvement['statut_entree']== 0:
                mouvement['statut_entree'] = 'NON CHARGE'
            elif mouvement['statut_entree'] == 1 :
                mouvement['statut_entree'] = 'NON CHARGE'
            else:
                mouvement['statut_entree'] = 'Vide'
                ################# STATUT SORTIE TEXT ###########
            if mouvement['statut_sortie'] == 0:
                 mouvement['statut_sortie'] = 'NON CHARGE'
            elif mouvement['statut_sortie'] == 1:
                 mouvement['statut_sortie'] = 'NON CHARGE'
            else:
                 mouvement['statut_sortie'] = 'Vide'
            ############## CAMION #####################
            camion_id = mouvement['camion_id']
            camion = Camion.objects.get(id_cam=camion_id)
            mouvement['transporteur'] = camion.transporteur
            mouvement['type'] = camion.type
            mouvement['immatriculation'] = camion.immatriculation
            ################### CHAUFFEUR ###################
            chauffeur_id = mouvement['chauffeur_id']
            chauffeur = Chaffeur.objects.get(id_chauffeur=chauffeur_id)
            mouvement['chauffeur_name'] = chauffeur.fullname
            mouvement['permis'] = chauffeur.permis
            ################## POINTEUR ENTREE ##############
            pointeur_entree_id = mouvement['pointeur_entree_id']
            Pointeur_entree = Utilisateurs.objects.get(id_user=pointeur_entree_id)
            mouvement['pointeur_entree_name'] = Pointeur_entree.fullname
            ################## POINTEUR SORTIE ##############
            pointeur_sortie_id = mouvement['pointeur_sortie_id']
            Pointeur_sortie = Utilisateurs.objects.get(id_user=pointeur_sortie_id)
            mouvement['pointeur_sortie_name'] = Pointeur_sortie.fullname
        # Créer un nouveau workbook Excel
        wb = Workbook()
        ws = wb.active
        ws.title = "Camions"
        ws.append([
            "Statut Entree", "Statut Sortie", "Camion", "Transporteur", "Type", "Remorque",
            "Chauffeur", "Permis", "Date Entrée", "Pointeur Entrée", "Date Sortie", "Pointeur Sortie", "mission"
        ])
        for mouvement in mouvement_list:
            ws.append([
                mouvement['statut_entree'], mouvement['statut_sortie'], mouvement['immatriculation'],
                mouvement['transporteur'], mouvement['type'], mouvement['remorque'],
                mouvement['chauffeur_name'], mouvement['permis'], str(mouvement['date_entree']),
                mouvement['pointeur_entree_name'], str(mouvement['date_sortie']), mouvement['pointeur_sortie_name'], mouvement['mission']
            ])
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="mouvements.xlsx"'

        wb.save(response)
        return response

    else:
        return HttpResponseBadRequest()


def export_mouvement1(request):
    if request.method == 'POST':
        # Récupérer les données des mouvements
        mouvements = Mouvement2.objects.filter(
            date_entree__isnull=False,
            date_sortie__isnull=False
        ).values(
            'id_mvt', 'chauffeur_id', 'camion_id', 'statut_entree', 'statut_sortie',
            'remorque', 'date_entree', 'pointeur_entree_id', 'date_sortie', 'pointeur_sortie_id','mission'
        )

        mouvement_list = list(mouvements)
        for mouvement in mouvement_list:
            ################# STATUT ENTREE TEXT ###########
            if mouvement['statut_entree']== 0:
                mouvement['statut_entree'] = 'NON CHARGE'
            elif mouvement['statut_entree'] == 1 :
                mouvement['statut_entree'] = 'NON CHARGE'
            else:
                mouvement['statut_entree'] = 'Vide'
                ################# STATUT SORTIE TEXT ###########
            if mouvement['statut_sortie'] == 0:
                 mouvement['statut_sortie'] = 'NON CHARGE'
            elif mouvement['statut_sortie'] == 1:
                 mouvement['statut_sortie'] = 'NON CHARGE'
            else:
                 mouvement['statut_sortie'] = 'Vide'
            ############## CAMION #####################
            camion_id = mouvement['camion_id']
            camion = Camion.objects.get(id_cam=camion_id)
            mouvement['transporteur'] = camion.transporteur
            mouvement['type'] = camion.type
            mouvement['immatriculation'] = camion.immatriculation
            ################### CHAUFFEUR ###################
            chauffeur_id = mouvement['chauffeur_id']
            chauffeur = Chaffeur.objects.get(id_chauffeur=chauffeur_id)
            mouvement['chauffeur_name'] = chauffeur.fullname
            mouvement['permis'] = chauffeur.permis
            ################## POINTEUR ENTREE ##############
            pointeur_entree_id = mouvement['pointeur_entree_id']
            Pointeur_entree = Utilisateurs.objects.get(id_user=pointeur_entree_id)
            mouvement['pointeur_entree_name'] = Pointeur_entree.fullname
            ################## POINTEUR SORTIE ##############
            pointeur_sortie_id = mouvement['pointeur_sortie_id']
            Pointeur_sortie = Utilisateurs.objects.get(id_user=pointeur_sortie_id)
            mouvement['pointeur_sortie_name'] = Pointeur_sortie.fullname
        # Créer un nouveau workbook Excel
        wb = Workbook()
        ws = wb.active
        ws.title = "Camions"
        ws.append([
            "Statut Entree", "Statut Sortie", "Camion", "Transporteur", "Type", "Remorque",
            "Chauffeur", "Permis", "Date Entrée", "Pointeur Entrée", "Date Sortie", "Pointeur Sortie", "mission"
        ])
        for mouvement in mouvement_list:
            ws.append([
                mouvement['statut_entree'], mouvement['statut_sortie'], mouvement['immatriculation'],
                mouvement['transporteur'], mouvement['type'], mouvement['remorque'],
                mouvement['chauffeur_name'], mouvement['permis'], str(mouvement['date_entree']),
                mouvement['pointeur_entree_name'], str(mouvement['date_sortie']), mouvement['pointeur_sortie_name'], mouvement['mission']
            ])
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="mouvements.xlsx"'

        wb.save(response)
        return response

    else:
        return HttpResponseBadRequest()


def liste_parametrage(request, id):
    user = get_object_or_404(Utilisateurs, id_user=id)
    if user.poste == 'A0':
        entite = 'dklog'
    elif user.poste == 'A1':
        entite = 'icdtom'
    elif user.poste == 'A2':
        entite = 'sacherie'
    listeboite = ParametrageDelais.objects.filter(entite=entite)
    return render(request, 'pages/parametrage1.html', {'boite': listeboite, 'util': user})


######################## AJOUT PARAMETRE #######################################
def ajouter_parametre(request):
    if request.method == 'POST':
        id_user = request.POST.get('id_user')
        util = get_object_or_404(Utilisateurs, id_user=id_user)

        entites = {
            'A0': 'dklog',
            'A1': 'icdtom',
            'A2': 'sacherie'
        }

        entite = entites.get(util.poste, None)
        if entite is None:
            return HttpResponse("Invalid user role", status=400)

        parametre, created = ParametrageDelais.objects.get_or_create(
            type=request.POST.get('type'),
            entite=entite
        )

        parametre.duree = request.POST.get('duree')
        parametre.type = request.POST.get('type')
        parametre.nbr_max = request.POST.get('nbr_max')
        parametre.entite = entite
        parametre.save()

        return redirect(f"/parametrage/{id_user}")
    else:
        return redirect(f"/doc/ajouterboite_page/{request.POST.get('id_user')}")

def modifier_parametre(request):
    if request.method == 'POST':
        boite_id = request.POST['boite_id']
        id_user = request.POST.get('id_user')
        parametre = get_object_or_404(ParametrageDelais, id_para=boite_id)
        parametre.duree = request.POST.get('duree')
        parametre.type = request.POST.get('type')
        parametre.nbr_max = request.POST.get('nbr_max')
        parametre.save()
        return redirect(f"/parametrage/{id_user}")

    return render(request, 'index.html')


# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from home.models import Utilisateurs, Mouvement1, Camion, Chaffeur
from django.contrib.auth.forms import AuthenticationForm
from .models import Utilisateurs

# myapp/forms.py
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
class MouvementForm(forms.ModelForm):
    class Meta:
        model = Mouvement1
        fields = ['statut_entree', 'camion', 'chauffeur']

    camion = forms.ModelChoiceField(queryset=Camion.objects.all(), empty_label="Select a camion")


class SortieForm(forms.ModelForm):
    class Meta:
        model = Mouvement1
        fields = ['camion', 'date_sortie', 'statut_sortie']

class ChauffeurForm(forms.ModelForm):
    class Meta:
        model = Chaffeur
        fields = ['fullname', 'permis']

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = ['immatriculation', 'transporteur', 'type']

class ExportForm(forms.Form):
    filename = forms.CharField(label='Nom du fichier', max_length=100)
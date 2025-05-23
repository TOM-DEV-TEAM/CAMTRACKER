# Generated by Django 4.2.9 on 2024-09-12 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id_cam', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
                ('immatriculation', models.CharField(max_length=20)),
                ('transporteur', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Chaffeur',
            fields=[
                ('id_chauffeur', models.AutoField(db_column='id_chauffeur', primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('permis', models.CharField(max_length=255, null=True)),
                ('telephone', models.CharField(max_length=255, null=True)),
                ('date_exp_permis', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.AutoField(db_column='id_client', primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mouvement0',
            fields=[
                ('id_mvt', models.AutoField(primary_key=True, serialize=False)),
                ('statut_entree', models.IntegerField(blank=True, null=True)),
                ('statut_sortie', models.IntegerField(blank=True, null=True)),
                ('date_sortie', models.DateTimeField(blank=True, null=True)),
                ('date_entree', models.DateTimeField(blank=True, null=True)),
                ('mission', models.CharField(max_length=255, null=True)),
                ('num_ticket', models.CharField(max_length=255, null=True)),
                ('code_camion', models.CharField(blank=True, null=True)),
                ('marchandise', models.CharField(max_length=255, null=True)),
                ('poids', models.CharField(blank=True, max_length=255, null=True)),
                ('poids_autorise', models.CharField(blank=True, max_length=255, null=True)),
                ('pont_bascule', models.IntegerField(blank=True, null=True)),
                ('destination_final', models.CharField(blank=True, max_length=255, null=True)),
                ('numconteneur1', models.CharField(max_length=255, null=True)),
                ('typeconteneur1', models.CharField(max_length=255, null=True)),
                ('numconteneur2', models.CharField(max_length=255, null=True)),
                ('typeconteneur2', models.CharField(max_length=255, null=True)),
                ('numconteneur3', models.CharField(max_length=255, null=True)),
                ('typeconteneur3', models.CharField(max_length=255, null=True)),
                ('pregate', models.CharField(max_length=255, null=True)),
                ('gatepass', models.CharField(max_length=255, null=True)),
                ('navire', models.CharField(blank=True, max_length=255, null=True)),
                ('bl1', models.CharField(blank=True, max_length=255, null=True)),
                ('bl2', models.CharField(blank=True, max_length=255, null=True)),
                ('date_validite', models.DateTimeField(blank=True, null=True)),
                ('nbrcolis', models.IntegerField(blank=True, null=True)),
                ('tonnage', models.IntegerField(blank=True, null=True)),
                ('remorque', models.CharField(max_length=255, null=True)),
                ('destination', models.CharField(max_length=255, null=True)),
                ('camion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements0', to='home.camion')),
                ('camionvrac', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements0vrac', to='home.camion')),
                ('chauffeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements0', to='home.chaffeur')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client0', to='home.client')),
            ],
        ),
        migrations.CreateModel(
            name='ParametrageDelais',
            fields=[
                ('id_para', models.AutoField(db_column='id_para', primary_key=True, serialize=False)),
                ('entite', models.CharField(max_length=255)),
                ('nbr_max', models.CharField(max_length=255, null=True)),
                ('type', models.CharField(max_length=20)),
                ('delais_maximal', models.CharField(max_length=20)),
                ('delais_urgent', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transitaire',
            fields=[
                ('id_transit', models.AutoField(db_column='id_transit', primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('mission', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateurs',
            fields=[
                ('id_user', models.AutoField(db_column='id_user', primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('matricule', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('poste', models.CharField(max_length=255)),
                ('status', models.CharField(default='active', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id_veh', models.AutoField(primary_key=True, serialize=False)),
                ('immatriculation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rejet',
            fields=[
                ('id_rejet', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('camion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.camion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.utilisateurs')),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id_observation', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('bd', models.IntegerField(blank=True, null=True)),
                ('dd', models.IntegerField(blank=True, null=True)),
                ('enpanne', models.IntegerField(blank=True, null=True)),
                ('motif_stationnement', models.CharField(blank=True, null=True)),
                ('camion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.camion')),
                ('id_mvt_0', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements3sdjhsdd', to='home.mouvement0')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.utilisateurs')),
            ],
        ),
        migrations.CreateModel(
            name='Mouvement8',
            fields=[
                ('id_mvt', models.AutoField(primary_key=True, serialize=False)),
                ('date_sortie', models.DateTimeField(blank=True, null=True)),
                ('date_entree', models.DateTimeField(blank=True, null=True)),
                ('destination', models.CharField(blank=True, null=True)),
                ('id_mvt_0', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvementsGHGHGHpart', to='home.mouvement0')),
                ('pointeur_entree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements7_entreepart', to='home.utilisateurs')),
                ('pointeur_sortie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements7_sortiepart', to='home.utilisateurs')),
                ('vehicule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvementsgttyyy2partveh', to='home.vehicule')),
            ],
        ),
        migrations.CreateModel(
            name='Mouvement7',
            fields=[
                ('id_mvt', models.AutoField(primary_key=True, serialize=False)),
                ('statut_entree', models.IntegerField(blank=True, null=True)),
                ('statut_sortie', models.IntegerField(blank=True, null=True)),
                ('date_sortie', models.DateTimeField(blank=True, null=True)),
                ('date_entree', models.DateTimeField(blank=True, null=True)),
                ('navire', models.CharField(blank=True, max_length=255, null=True)),
                ('poids', models.CharField(blank=True, max_length=255, null=True)),
                ('poids_autorise', models.CharField(blank=True, max_length=255, null=True)),
                ('pont_bascule', models.IntegerField(blank=True, null=True)),
                ('destination', models.CharField(blank=True, max_length=255, null=True)),
                ('bl1', models.CharField(blank=True, max_length=255, null=True)),
                ('bl2', models.CharField(blank=True, max_length=255, null=True)),
                ('nbrcolis', models.IntegerField(blank=True, null=True)),
                ('tonnage', models.IntegerField(blank=True, null=True)),
                ('marchandise', models.CharField(blank=True, max_length=255, null=True)),
                ('remorque', models.CharField(max_length=255, null=True)),
                ('mission', models.CharField(max_length=255, null=True)),
                ('camion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvementsgttyyy2', to='home.camion')),
                ('chauffeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvementsGJGGUGJ', to='home.chaffeur')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client7', to='home.client')),
                ('id_mvt_0', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvementsGHGHGH', to='home.mouvement0')),
                ('pointeur_entree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements7_entree', to='home.utilisateurs')),
                ('pointeur_sortie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements7_sortie', to='home.utilisateurs')),
            ],
        ),
        migrations.CreateModel(
            name='Mouvement6',
            fields=[
                ('id_mvt', models.AutoField(primary_key=True, serialize=False)),
                ('statut_entree', models.IntegerField(blank=True, null=True)),
                ('statut_sortie', models.IntegerField(blank=True, null=True)),
                ('date_sortie', models.DateTimeField(blank=True, null=True)),
                ('date_entree', models.DateTimeField(blank=True, null=True)),
                ('navire', models.CharField(blank=True, max_length=255, null=True)),
                ('bl1', models.CharField(blank=True, max_length=255, null=True)),
                ('bl2', models.CharField(blank=True, max_length=255, null=True)),
                ('poids', models.CharField(blank=True, max_length=255, null=True)),
                ('poids_autorise', models.CharField(blank=True, max_length=255, null=True)),
                ('pont_bascule', models.IntegerField(blank=True, null=True)),
                ('destination', models.CharField(blank=True, max_length=255, null=True)),
                ('nbrcolis', models.IntegerField(blank=True, null=True)),
                ('tonnage', models.IntegerField(blank=True, null=True)),
                ('marchandise', models.CharField(blank=True, max_length=255, null=True)),
                ('remorque', models.CharField(max_length=255, null=True)),
                ('mission', models.CharField(max_length=255, null=True)),
                ('camion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements', to='home.camion')),
                ('chauffeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvementsgchghhgghghhghg', to='home.chaffeur')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client6', to='home.client')),
                ('id_mvt_0', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvementsggggff', to='home.mouvement0')),
                ('pointeur_entree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements6_entree', to='home.utilisateurs')),
                ('pointeur_sortie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements6_sortie', to='home.utilisateurs')),
            ],
        ),
        migrations.CreateModel(
            name='Mouvement5',
            fields=[
                ('id_mvt', models.AutoField(primary_key=True, serialize=False)),
                ('statut_entree', models.IntegerField(blank=True, null=True)),
                ('statut_sortie', models.IntegerField(blank=True, null=True)),
                ('date_sortie', models.DateTimeField(blank=True, null=True)),
                ('date_entree', models.DateTimeField(blank=True, null=True)),
                ('navire', models.CharField(blank=True, max_length=255, null=True)),
                ('bl1', models.CharField(blank=True, max_length=255, null=True)),
                ('bl2', models.CharField(blank=True, max_length=255, null=True)),
                ('nbrcolis', models.IntegerField(blank=True, null=True)),
                ('tonnage', models.IntegerField(blank=True, null=True)),
                ('marchandise', models.CharField(blank=True, max_length=255, null=True)),
                ('remorque', models.CharField(max_length=255, null=True)),
                ('mission', models.CharField(max_length=255, null=True)),
                ('camion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='camionmouvements5', to='home.camion')),
                ('chauffeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chauffeurmouvementstyy', to='home.chaffeur')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client5', to='home.client')),
                ('id_mvt_0', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvementshggy', to='home.mouvement0')),
                ('pointeur_entree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements5_entree', to='home.utilisateurs')),
                ('pointeur_sortie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements5_sortie', to='home.utilisateurs')),
            ],
        ),
        migrations.CreateModel(
            name='Mouvement4',
            fields=[
                ('id_mvt', models.AutoField(primary_key=True, serialize=False)),
                ('statut_entree', models.IntegerField(blank=True, null=True)),
                ('statut_sortie', models.IntegerField(blank=True, null=True)),
                ('date_sortie', models.DateTimeField(blank=True, null=True)),
                ('date_entree', models.DateTimeField(blank=True, null=True)),
                ('remorque', models.CharField(max_length=255, null=True)),
                ('mission', models.CharField(max_length=255, null=True)),
                ('camion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='camionmouvements4', to='home.camion')),
                ('chauffeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chauffeurmouvements4', to='home.chaffeur')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client4', to='home.client')),
                ('id_mvt_0', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvementsTY', to='home.mouvement0')),
                ('pointeur_entree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements_entree4', to='home.utilisateurs')),
                ('pointeur_sortie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements_sortie4', to='home.utilisateurs')),
            ],
        ),
        migrations.CreateModel(
            name='Mouvement3',
            fields=[
                ('id_mvt', models.AutoField(primary_key=True, serialize=False)),
                ('statut_entree', models.IntegerField(blank=True, null=True)),
                ('statut_sortie', models.IntegerField(blank=True, null=True)),
                ('date_sortie', models.DateTimeField(blank=True, null=True)),
                ('date_entree', models.DateTimeField(blank=True, null=True)),
                ('num_ticket', models.CharField(max_length=255, null=True)),
                ('date_validite', models.DateTimeField(blank=True, null=True)),
                ('marchandise', models.CharField(max_length=255, null=True)),
                ('numconteneur1', models.CharField(max_length=255, null=True)),
                ('typeconteneur1', models.CharField(max_length=255, null=True)),
                ('numconteneur2', models.CharField(max_length=255, null=True)),
                ('typeconteneur2', models.CharField(max_length=255, null=True)),
                ('numconteneur3', models.CharField(max_length=255, null=True)),
                ('typeconteneur3', models.CharField(max_length=255, null=True)),
                ('pregate', models.CharField(max_length=255, null=True)),
                ('gatepass', models.CharField(max_length=255, null=True)),
                ('remorque', models.CharField(max_length=255, null=True)),
                ('mission', models.CharField(max_length=255, null=True)),
                ('camion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements3', to='home.camion')),
                ('chauffeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements3', to='home.chaffeur')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client3', to='home.client')),
                ('id_mvt_0', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements3', to='home.mouvement0')),
                ('pointeur_entree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements_entree3', to='home.utilisateurs')),
                ('pointeur_sortie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements_sortie3', to='home.utilisateurs')),
            ],
        ),
        migrations.CreateModel(
            name='Mouvement2',
            fields=[
                ('id_mvt', models.AutoField(primary_key=True, serialize=False)),
                ('statut_entree', models.IntegerField(blank=True, null=True)),
                ('statut_sortie', models.IntegerField(blank=True, null=True)),
                ('date_sortie', models.DateTimeField(blank=True, null=True)),
                ('date_entree', models.DateTimeField(blank=True, null=True)),
                ('poids', models.CharField(blank=True, max_length=255, null=True)),
                ('poids_autorise', models.CharField(blank=True, max_length=255, null=True)),
                ('pont_bascule', models.IntegerField(blank=True, null=True)),
                ('destination', models.CharField(blank=True, max_length=255, null=True)),
                ('code_camion', models.CharField(blank=True, null=True)),
                ('remorque', models.CharField(max_length=255, null=True)),
                ('mission', models.CharField(max_length=255, null=True)),
                ('camion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements2GHGH', to='home.camion')),
                ('chauffeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements2GJUGJG', to='home.chaffeur')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client2', to='home.client')),
                ('id_mvt_0', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements2GHGHGP', to='home.mouvement0')),
                ('pointeur_entree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements2_entree2', to='home.utilisateurs')),
                ('pointeur_sortie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements2_sortie2', to='home.utilisateurs')),
            ],
        ),
        migrations.CreateModel(
            name='Mouvement1',
            fields=[
                ('id_mvt', models.AutoField(primary_key=True, serialize=False)),
                ('statut_entree', models.IntegerField(blank=True, null=True)),
                ('statut_sortie', models.IntegerField(blank=True, null=True)),
                ('date_sortie', models.DateTimeField(blank=True, null=True)),
                ('date_entree', models.DateTimeField(blank=True, null=True)),
                ('remorque', models.CharField(max_length=255, null=True)),
                ('mission', models.CharField(max_length=255, null=True)),
                ('camion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='camionsNNmouvements1', to='home.camion')),
                ('chauffeur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chauffeurmouvemeNNnts1', to='home.chaffeur')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client1', to='home.client')),
                ('id_mvt_0', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements1', to='home.mouvement0')),
                ('pointeur_entree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements_entree1', to='home.utilisateurs')),
                ('pointeur_sortie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements_sortie1', to='home.utilisateurs')),
            ],
        ),
        migrations.AddField(
            model_name='mouvement0',
            name='pointeur_entree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements_entree0', to='home.utilisateurs'),
        ),
        migrations.AddField(
            model_name='mouvement0',
            name='pointeur_sortie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements_sortie0', to='home.utilisateurs'),
        ),
        migrations.AddField(
            model_name='mouvement0',
            name='transitaire',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mouvements0', to='home.transitaire'),
        ),
        migrations.AddField(
            model_name='mouvement0',
            name='vehicule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modffsuvementsgttyyy2partveh', to='home.vehicule'),
        ),
    ]

# Generated by Django 4.2.4 on 2024-03-30 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_remove_coefficient_classe_remove_coefficient_filiere_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='devoirNote',
            new_name='devoir',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='matiereNote',
            new_name='matiere',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='trimestreDevoir',
            new_name='trimestre',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='valeurNote',
            new_name='valeur',
        ),
        migrations.AlterUniqueTogether(
            name='note',
            unique_together={('matiere', 'devoir', 'trimestre', 'eleve')},
        ),
    ]
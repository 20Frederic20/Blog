# Generated by Django 4.2.4 on 2024-03-31 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_remove_coefficient_classe_remove_coefficient_filiere_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='coefficient',
            unique_together={('matiere', 'filiere', 'classe')},
        ),
    ]
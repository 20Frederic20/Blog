# Generated by Django 4.2.4 on 2024-04-01 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_rename_codedevoir_devoir_code_and_more'),
        ('users', '0002_rename_devoirnote_note_devoir_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eleve',
            unique_together={('user', 'filiere', 'classe', 'promotion')},
        ),
    ]

# Generated by Django 4.2.4 on 2024-04-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_promotions', '0006_alter_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mother_contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='tutor_contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

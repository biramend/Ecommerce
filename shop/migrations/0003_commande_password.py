# Generated by Django 3.1.4 on 2021-10-04 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='password',
            field=models.CharField(default='pass123', max_length=150),
        ),
    ]

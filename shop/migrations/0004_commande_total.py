# Generated by Django 3.1.4 on 2021-10-05 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_commande_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='total',
            field=models.CharField(default='500', max_length=300),
            preserve_default=False,
        ),
    ]

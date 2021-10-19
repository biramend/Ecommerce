# Generated by Django 3.1.4 on 2021-10-04 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=300)),
                ('nom', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=250, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('adresse', models.CharField(max_length=150)),
                ('ville', models.CharField(max_length=150)),
                ('pays', models.CharField(max_length=150)),
                ('zipcode', models.CharField(max_length=150)),
                ('date_commade', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_commade'],
            },
        ),
    ]

# Generated by Django 3.2.3 on 2022-02-16 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='batchno',
            field=models.CharField(max_length=10),
        ),
    ]

# Generated by Django 5.0.6 on 2024-09-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raidlogix', '0006_alter_risk_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='score',
            field=models.CharField(max_length=50),
        ),
    ]
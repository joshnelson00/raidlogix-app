# Generated by Django 5.0.6 on 2024-07-11 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raidlogix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('state', models.CharField(max_length=50)),
                ('action_source', models.CharField(max_length=50)),
                ('importance', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.project')),
            ],
        ),
        migrations.CreateModel(
            name='assumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('updated', models.TextField()),
                ('item', models.TextField()),
                ('notes', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.project')),
            ],
        ),
        migrations.CreateModel(
            name='decision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('due', models.DateField()),
                ('state', models.CharField(max_length=50)),
                ('decision_made', models.CharField(max_length=50)),
                ('justification', models.TextField()),
                ('impact', models.TextField()),
                ('importance', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.project')),
            ],
        ),
        migrations.CreateModel(
            name='issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('impact_details', models.TextField()),
                ('state', models.CharField(max_length=50)),
                ('importance', models.IntegerField()),
                ('impact', models.IntegerField()),
                ('response_status', models.TextField()),
                ('resolution', models.TextField()),
                ('date_resolved', models.DateField()),
                ('root_cause', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.project')),
            ],
        ),
        migrations.CreateModel(
            name='risk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('owner', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('probability', models.IntegerField()),
                ('impact', models.IntegerField()),
                ('score', models.IntegerField()),
                ('date_raised', models.DateField()),
                ('trigger_date', models.DateField()),
                ('date_closed', models.DateField()),
                ('response_strategy', models.CharField(max_length=50)),
                ('response_plan_state', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.project')),
            ],
        ),
    ]
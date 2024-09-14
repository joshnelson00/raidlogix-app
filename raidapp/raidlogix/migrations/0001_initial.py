# Generated by Django 5.0.6 on 2024-09-14 18:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('budget', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('impact_details', models.TextField()),
                ('state', models.CharField(max_length=50)),
                ('importance', models.IntegerField()),
                ('impact', models.IntegerField()),
                ('response_status', models.TextField()),
                ('resolution', models.TextField()),
                ('root_cause', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.project')),
            ],
        ),
        migrations.CreateModel(
            name='dependency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('budget', models.FloatField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.project')),
            ],
        ),
        migrations.CreateModel(
            name='decision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('state', models.CharField(max_length=50)),
                ('decision_made', models.CharField(max_length=50)),
                ('justification', models.TextField()),
                ('impact', models.TextField()),
                ('importance', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.project')),
            ],
        ),
        migrations.CreateModel(
            name='assumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('updated', models.TextField()),
                ('item', models.TextField()),
                ('notes', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.project')),
            ],
        ),
        migrations.CreateModel(
            name='action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('state', models.CharField(max_length=50)),
                ('action_source', models.CharField(max_length=50)),
                ('importance', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.project')),
            ],
        ),
        migrations.CreateModel(
            name='risk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('owner', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('probability', models.IntegerField()),
                ('impact', models.IntegerField()),
                ('score', models.IntegerField()),
                ('response_strategy', models.CharField(max_length=50)),
                ('response_plan_state', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.project')),
            ],
        ),
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.project')),
            ],
        ),
        migrations.CreateModel(
            name='risk_tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.risk')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.tag')),
            ],
        ),
        migrations.CreateModel(
            name='issue_tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.issue')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.tag')),
            ],
        ),
        migrations.CreateModel(
            name='decision_tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.decision')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.tag')),
            ],
        ),
        migrations.CreateModel(
            name='assumption_tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assumption', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.assumption')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.tag')),
            ],
        ),
        migrations.CreateModel(
            name='action_tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.action')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.tag')),
            ],
        ),
        migrations.CreateModel(
            name='user_decisions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('decision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.decision')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='user_projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raidlogix.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

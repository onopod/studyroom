# Generated by Django 5.0.4 on 2024-05-03 23:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=400)),
                ('emote', models.CharField(max_length=10, null=True)),
                ('chara', models.CharField(max_length=10, null=True)),
                ('place', models.CharField(max_length=10, null=True)),
                ('subject', models.CharField(default='指定なし', max_length=100)),
                ('comment', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('arg1', models.CharField(max_length=100, null=True)),
                ('arg2', models.CharField(max_length=100, null=True)),
                ('arg3', models.CharField(max_length=100, null=True)),
                ('arg4', models.CharField(max_length=100, null=True)),
                ('executed_unity', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
    ]

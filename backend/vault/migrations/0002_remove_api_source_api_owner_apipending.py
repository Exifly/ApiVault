# Generated by Django 4.2.2 on 2023-06-24 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vault', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api',
            name='source',
        ),
        migrations.AddField(
            model_name='api',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='APIPending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('auth', models.CharField(choices=[('apiKey', 'apiKey'), ('OAuth', 'OAuth'), ('', 'None')], max_length=100)),
                ('cors', models.BooleanField()),
                ('description', models.TextField()),
                ('https', models.BooleanField()),
                ('url', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vault.category')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

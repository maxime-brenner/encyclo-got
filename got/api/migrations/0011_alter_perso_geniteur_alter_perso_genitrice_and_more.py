# Generated by Django 4.1.4 on 2022-12-17 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_maison_membre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perso',
            name='geniteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Père', to='api.perso', verbose_name='Père'),
        ),
        migrations.AlterField(
            model_name='perso',
            name='genitrice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Mère', to='api.perso', verbose_name='Mère'),
        ),
        migrations.AlterField(
            model_name='perso',
            name='isnoble',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='perso',
            name='maisonnaissance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Maison de naissance+', to='api.maison', verbose_name='Maison de naissance'),
        ),
    ]

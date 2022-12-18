# Generated by Django 4.1.4 on 2022-12-17 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_perso_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perso',
            name='geniteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Père', to='api.perso'),
        ),
        migrations.AlterField(
            model_name='perso',
            name='genitrice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Mère', to='api.perso'),
        ),
    ]

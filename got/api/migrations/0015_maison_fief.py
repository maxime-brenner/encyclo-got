# Generated by Django 4.1.4 on 2022-12-17 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_continent_alter_maison_banneret_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maison',
            name='fief',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Fief', to='api.lieu'),
        ),
    ]

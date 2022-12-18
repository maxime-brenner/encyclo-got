# Generated by Django 4.1.4 on 2022-12-17 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_perso_surnom_alter_perso_nombatard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom')),
            ],
        ),
        migrations.AlterField(
            model_name='maison',
            name='banneret',
            field=models.ManyToManyField(blank=True, to='api.maison'),
        ),
        migrations.AlterField(
            model_name='maison',
            name='suzerain',
            field=models.ManyToManyField(blank=True, to='api.maison'),
        ),
        migrations.CreateModel(
            name='Lieu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, verbose_name='Nom')),
                ('continent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Continent', to='api.continent')),
            ],
        ),
        migrations.AddField(
            model_name='continent',
            name='lieu',
            field=models.ManyToManyField(related_name='Lieu', to='api.lieu'),
        ),
    ]

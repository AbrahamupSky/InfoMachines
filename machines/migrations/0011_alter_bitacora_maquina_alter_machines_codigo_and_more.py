# Generated by Django 4.2.5 on 2023-12-07 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0010_alter_bitacora_maquina_alter_machines_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitacora',
            name='maquina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='machines.machines', to_field='codigo'),
        ),
        migrations.AlterField(
            model_name='machines',
            name='codigo',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='machines',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

# Generated by Django 4.1.4 on 2023-02-04 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ric', '0005_alter_radar_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radar',
            name='data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]

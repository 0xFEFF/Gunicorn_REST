# Generated by Django 3.1 on 2020-08-17 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pc_shop', '0002_auto_20200816_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prozessor',
            options={'ordering': ['Modell']},
        ),
    ]

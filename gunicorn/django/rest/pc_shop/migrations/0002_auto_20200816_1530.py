# Generated by Django 3.1 on 2020-08-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prozessor',
            name='Kerne',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='prozessor',
            name='Threads',
            field=models.IntegerField(),
        ),
    ]
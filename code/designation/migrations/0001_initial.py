# Generated by Django 4.2.5 on 2023-09-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designação',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidade', models.CharField(max_length=250)),
                ('designacao', models.CharField(max_length=250)),
            ],
        ),
    ]
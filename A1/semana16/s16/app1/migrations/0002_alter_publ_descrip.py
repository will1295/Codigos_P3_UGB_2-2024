# Generated by Django 5.1.3 on 2024-11-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publ',
            name='descrip',
            field=models.CharField(max_length=300),
        ),
    ]
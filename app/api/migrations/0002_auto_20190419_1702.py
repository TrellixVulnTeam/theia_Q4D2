# Generated by Django 2.2 on 2019-04-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageryrequest',
            name='kml_polygon',
            field=models.TextField(null=True),
        ),
    ]

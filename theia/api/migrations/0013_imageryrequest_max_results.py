# Generated by Django 2.2.2 on 2019-06-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_pipelinestage_output_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageryrequest',
            name='max_results',
            field=models.IntegerField(null=True),
        ),
    ]
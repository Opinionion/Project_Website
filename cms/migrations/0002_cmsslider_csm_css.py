# Generated by Django 4.0.6 on 2022-07-07 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='csm_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='Css class'),
        ),
    ]

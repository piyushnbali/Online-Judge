# Generated by Django 2.1.5 on 2019-02-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('round2', '0005_score_language_prefered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='language_prefered',
        ),
        migrations.AddField(
            model_name='score',
            name='language_preferred',
            field=models.CharField(default='c', max_length=50),
        ),
    ]

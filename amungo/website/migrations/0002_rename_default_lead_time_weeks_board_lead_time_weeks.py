# Generated by Django 4.0.5 on 2022-06-30 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='default_lead_time_weeks',
            new_name='lead_time_weeks',
        ),
    ]

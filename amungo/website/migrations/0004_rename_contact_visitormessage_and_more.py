# Generated by Django 4.0.5 on 2022-06-30 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_contact_alter_boardphoto_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='VisitorMessage',
        ),
        migrations.AlterModelOptions(
            name='visitormessage',
            options={'verbose_name': 'сообщение посетителя', 'verbose_name_plural': 'сообщения посетителей'},
        ),
    ]
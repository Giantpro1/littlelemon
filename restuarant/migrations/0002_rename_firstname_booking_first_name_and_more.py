# Generated by Django 4.2.7 on 2023-11-21 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restuarant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='reservationdate',
            new_name='reservation_date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='reservationslot',
            new_name='reservation_slot',
        ),
    ]

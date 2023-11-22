# Generated by Django 4.2.7 on 2023-11-21 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('reservationdate', models.DateField()),
                ('reservationslot', models.SmallIntegerField(default=10)),
            ],
            options={
                'verbose_name_plural': 'Booking',
            },
        ),
    ]

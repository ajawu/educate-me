# Generated by Django 3.1.3 on 2020-12-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pledge_donations', '0003_contact_has_reached_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='donation_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-17 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='books/')),
                ('total_donated', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=150)),
                ('contact_email', models.EmailField(max_length=254)),
                ('message_title', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=400)),
                ('venue_state', models.CharField(max_length=20)),
                ('venue_lga', models.CharField(max_length=100)),
                ('venue_street_address', models.CharField(max_length=300)),
                ('event_time', models.DateTimeField(auto_now_add=True)),
                ('books', models.ManyToManyField(related_name='events', to='pledge_donations.Books')),
                ('volunteers', models.ManyToManyField(related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20)),
                ('donation_time', models.DateTimeField(auto_now_add=True)),
                ('donation_type', models.CharField(max_length=5)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='donations', to='pledge_donations.books')),
                ('donor', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='donations', to='pledge_donations.event')),
            ],
        ),
    ]

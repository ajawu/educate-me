# Generated by Django 3.1.3 on 2020-12-17 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pledge_donations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

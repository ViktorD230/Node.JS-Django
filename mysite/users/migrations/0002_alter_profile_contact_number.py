# Generated by Django 5.0.4 on 2024-04-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(default='+3800000000', max_length=50),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-26 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_director_born_alter_actor_born_alter_actor_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='born',
        ),
    ]

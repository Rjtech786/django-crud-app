# Generated by Django 4.2.7 on 2023-11-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0005_alter_studentdata_passw_alter_studentdata_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='studentdata',
        ),
    ]

# Generated by Django 4.2b1 on 2023-04-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppKaren', '0009_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('texto', models.CharField(max_length=150)),
            ],
        ),
    ]
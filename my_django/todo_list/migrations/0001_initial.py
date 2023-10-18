# Generated by Django 4.2.5 on 2023-10-11 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=121)),
                ('active', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('owner', models.CharField(max_length=121)),
                ('create_data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

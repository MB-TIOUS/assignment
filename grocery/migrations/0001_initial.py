# Generated by Django 3.2.6 on 2021-08-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='list_element',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('un', models.CharField(max_length=100)),
                ('iname', models.CharField(max_length=100)),
                ('iquantity', models.CharField(max_length=100)),
                ('istatus', models.CharField(max_length=100)),
                ('idate', models.DateField()),
            ],
        ),
    ]
# Generated by Django 3.2.3 on 2021-05-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

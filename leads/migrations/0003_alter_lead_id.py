# Generated by Django 3.2.3 on 2021-05-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_alter_lead_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-29 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('milk', '0007_auto_20200526_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milk.Supplier', unique_for_date='date'),
        ),
    ]

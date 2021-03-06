# Generated by Django 3.0.6 on 2020-05-22 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('rent', models.FloatField()),
                ('rent_type', models.CharField(default='A', max_length=1)),
                ('rent_date', models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='occupency',
            name='rent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenancy.Propery'),
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-25 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milk', '0003_auto_20200525_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='remark',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

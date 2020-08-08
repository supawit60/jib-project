# Generated by Django 3.1 on 2020-08-08 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0003_auto_20200808_0635'),
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='worker',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='workers.worker'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfume', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfume',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='accord',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='designer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='perfume',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

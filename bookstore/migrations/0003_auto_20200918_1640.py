# Generated by Django 3.1.1 on 2020-09-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20200918_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

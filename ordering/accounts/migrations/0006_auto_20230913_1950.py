# Generated by Django 3.2.12 on 2023-09-13 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20230913_1852'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OverallOrderStatus',
        ),
        migrations.DeleteModel(
            name='TagColors',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]

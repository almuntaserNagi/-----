# Generated by Django 4.2 on 2023-09-01 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customer_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='stop_at',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='نم الوقوف في'),
        ),
    ]
